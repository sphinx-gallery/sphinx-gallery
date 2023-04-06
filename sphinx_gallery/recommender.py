# -*- coding: utf-8 -*-
# Author: Arturo Amor
# License: 3-clause BSD
"""
Recommendation generator
========================

Generate content based KNN recommendation system
"""
# %%
import re
import os
from collections import defaultdict
from pathlib import Path

import numpy as np
import scipy.sparse as sp

from scipy.sparse.linalg import norm
from .backreferences import _thumbnail_div, THUMBNAIL_PARENT_DIV, THUMBNAIL_PARENT_DIV_CLOSE
from .py_source_parser import split_code_and_text_blocks
from .gen_rst import extract_intro_and_title


def tokenize(doc):
    """Extract tokens from doc.

    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer or
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))


def token_freqs(doc):
    """Extract a dict mapping raw tokens from doc to their occurrences."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq


def dict_freqs(doc):
    """Extract a dict mapping list of tokens to their occurrences."""

    freq = defaultdict(int)
    for tok in doc:
        freq[tok] += 1
    return freq


def dict_vectorizer(data_dict):
    """
    Convert a dictionary of feature arrays into a sparse matrix.

    Parameters
    ----------
    data_dict : dict
        A dictionary of feature arrays, where each key corresponds to a feature
        name, and each value is an array of feature values.

    Returns
    -------
    X : scipy.sparse matrix
        A sparse matrix in CSR format of shape (n_samples, n_features) where n_samples is the
        number of samples in the dataset and n_features is the total number of
        features across all samples.
    """
    feature_names = []
    all_values = defaultdict(list)
    for row in data_dict:
        for feature_name, feature_value in row.items():
            feature_names.append(feature_name)
            all_values[feature_name].append(feature_value)

    feature_names = list(set(feature_names))
    feature_names.sort()
    data = []
    indices = []
    indptr = [0]
    for i, row in enumerate(data_dict):
        for j, feature_name in enumerate(feature_names):
            if feature_name in row:
                feature_value = row[feature_name]
                data.append(feature_value)
                indices.append(j)
        indptr.append(len(indices))
    X = sp.csr_matrix(
        (data, indices, indptr), shape=(len(indptr) - 1, len(feature_names))
    )
    return X


def tfidf_transformer(X):
    """
    Transform a term frequency matrix into a term frequency-inverse document
    frequency (tf-idf) matrix.

    Parameters
    ----------
    X : numpy array or scipy sparse matrix
        A term frequency matrix of shape (n_samples, n_features) where n_samples
        is the number of samples in the dataset and n_features is the total number
        of distinct terms across all samples.

    Returns
    -------
    X_tfidf : numpy array or scipy sparse matrix
        A tf-idf matrix of the same shape as X.
    """
    FLOAT_DTYPES = (np.float64, np.float32, np.float16)

    if not sp.issparse(X):
        X = sp.csr_matrix(X, dtype=np.float64)
    dtype = X.dtype if X.dtype in FLOAT_DTYPES else np.float64

    n_samples, n_features = X.shape

    # Count the number of non-zero values for each feature in sparse X
    if sp.isspmatrix_csr(X):
        df = np.bincount(X.indices, minlength=n_features)
    else:
        df = np.diff(X.indptr)
    df = df.astype(dtype, copy=False)
    # perform idf smoothing
    df += 1
    n_samples += 1
    idf = np.log(n_samples / df) + 1

    idf_diag = sp.diags(
        idf,
        offsets=0,
        shape=(n_features, n_features),
        format="csr",
        dtype=dtype,
    )
    X = X * idf_diag
    X_normalized = (X.T / norm(X, axis=1)).T
    X_normalized = sp.csr_matrix(X_normalized, dtype=np.float64)

    return X_normalized


def cosine_similarity(X, Y=None, dense_output=True):
    """
    Compute the cosine similarity between two vectors X and Y.

    Parameters
    ----------
    X : {ndarray, sparse matrix}

    Y : {ndarray, sparse matrix}, default=None
        Input data. If ``None``, the output will be the pairwise
        similarities between all samples in ``X``.

    dense_output : bool, default=True
        Whether to return dense output even when the input is sparse. If
        ``False``, the output is sparse if both input arrays are sparse.

    Returns
    -------
    The cosine similarity between vectors X and Y
    """

    if Y is X or Y is None:
        Y = X

    X_normalized = X / norm(X)
    if X is Y:
        Y_normalized = X_normalized
    else:
        Y_normalized = Y / norm(Y)

    X_normalized = sp.csr_matrix(X_normalized, dtype=np.float64)
    similarity = X_normalized @ Y_normalized.T

    if dense_output and hasattr(similarity, "toarray"):
        return similarity.toarray()
    return similarity


class ExampleRecommender():
    """
    Compute content-based knn-tfidf recommendation system.

    Parameters
    ----------
    n_examples : int, default=5
        Number of most relevant examples to display.

    tokens : {"raw", "backrefs"}, default="raw"
        Whether to tokenize raw full text or create dictionary from list of
        backreferences.

    Attributes
    ----------
    similarity_matrix_ : sparse matrix
        Name of the file corresponding to the query index `item_id`.
    """
    def __init__(self, *, n_examples=5, tokens="raw"):
        self.n_examples = n_examples
        self.tokens = tokens

    # @staticmethod
    # def _load_data(listdir, tokens):
    #     rootdir = "/home/arturoamor/scikit-learn/doc/auto_examples/"
    #     data = {"file_name": [], "content": []}
    #     if tokens == "raw":
    #         for subdir, dirs, files in os.walk(rootdir):
    #             for file in os.listdir(subdir):
    #                 if file.endswith(".py"):
    #                     file_name = os.path.join(subdir, file)
    #                     data["file_name"].append(file_name.split(".py")[0])
    #                     data["content"].append(Path(file_name).read_text())
    #                 else:
    #                     continue
    #     # elif tokens == "backrefs":
    #     #     for subdir, dirs, files in os.walk(rootdir):
    #     #         for file in os.listdir(subdir):
    #     #             if file.endswith(".pickle"):
    #     #                 file_name = os.path.join(subdir, file)
    #     #                 with open(file_name, "rb") as f:
    #     #                     names = pickle.load(f)
    #     #                 back_references = [name.split("_codeobj")[0] for name in names.keys()]
    #     #                 data["file_name"].append(file_name.split("_codeobj")[0])
    #     #                 data["content"].append(back_references)
    #     #             else:
    #     #                 continue
    #     else:
    #         raise NotImplementedError

    
    def fit(self, file_names):
        """
        Compute the similarity matrix of a group of documents.

        Parameters
        ----------
        file_names : list or generator of file names.

        Returns
        -------
        self : object
            Fitted recommender.
        """
        if self.tokens == "raw":
            counts_matrix = dict_vectorizer(
                [token_freqs(Path(fname).read_text()) for fname in file_names]
            )
        # elif self.tokens == "backrefs":
        #     counts_matrix = dict_vectorizer(
        #         [dict_freqs(Path(fname).read_text()) for fname in data]
        #     )
        else:
            raise ValueError(
                "Value not supported. Possible values for tokens are 'raw' and 'backrefs'"
            )
        tfidf_matrix = tfidf_transformer(counts_matrix)
        self.similarity_matrix_ = cosine_similarity(tfidf_matrix)
        self.file_names_ = file_names
        return self

    def predict(self, file_name):
        """
        Given an item id, compute nearest neighbors.

        Parameters
        ----------
        file_name : str
            Name of the file corresponding to the query index `item_id`.

        item_id : int
            Index of the item to query.

        Returns
        -------
        recommendations : list of str
            Name of the files most similar to the query.
        """
        n_examples = self.n_examples
        similarity_matrix = self.similarity_matrix_
        file_names = self.file_names_
        item_id = file_names.index(file_name)
        similar_items = list(enumerate(similarity_matrix[item_id]))
        sorted_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

        # Get the top k items similar to item_id
        top_k_items = [index for index, value in sorted_items[1 : n_examples + 1]]
        query = file_name
        recommendations = [file_names[index] for index in top_k_items]
        return query, recommendations


def _write_recommendations(recommender, fname, gallery_conf):
    src_dir = gallery_conf["src_dir"]
    include_path = os.path.join("%s.recommendations" % fname[:-3])
    _, recommendations = recommender.predict(fname)

    with open(include_path, "w", encoding="utf-8") as ex_file:
        ex_file.write("\n\n.. rubric:: Related examples\n")
        ex_file.write(THUMBNAIL_PARENT_DIV)
        for recommendation in recommendations:
            rec_path, rec_name = recommendation.rsplit("/", maxsplit=1)
            _, script_blocks = split_code_and_text_blocks(
                recommendation, return_node=False)
            intro, title = extract_intro_and_title(fname, script_blocks[0][1])
            ex_file.write(
                _thumbnail_div(
                    rec_path,
                    src_dir,
                    rec_name,
                    intro,
                    title,
                    is_backref=True,
                )
            )
        ex_file.write(THUMBNAIL_PARENT_DIV_CLOSE)

# # %%
# rootdir = "/home/arturoamor/scikit-learn/doc/auto_examples/"
# data = {"file_name": [], "content": []}

# for subdir, dirs, files in os.walk(rootdir):
#     for file in os.listdir(subdir):
#         if file.endswith(".py"):
#             file_name = os.path.join(subdir, file)
#             data["file_name"].append(file_name.split(".py")[0])
#             data["content"].append(Path(file_name).read_text())
#         else:
#             continue

# recommender = ExampleRecommender(n_examples=5, tokens="raw")
# recommender.fit(data)
# query, recommendations = recommender.predict(data, item_id=12)

# print(f"Query: {query}")
# print("Recommendations:")
# for recommendation in recommendations:
#     print(f"\t- {recommendation.split('/')[-1]}")

# # %%
# rootdir = "/home/arturoamor/scikit-learn/doc/auto_examples/"
# data = {"file_name": [], "content": []}

# for subdir, dirs, files in os.walk(rootdir):
#     for file in os.listdir(subdir):
#         if file.endswith(".pickle"):
#             file_name = os.path.join(subdir, file)
#             with open(file_name, "rb") as f:
#                 names = pickle.load(f)
#             back_references = [name.split("_codeobj")[0] for name in names.keys()]
#             data["file_name"].append(file_name.split("_codeobj")[0])
#             data["content"].append(back_references)
#         else:
#             continue

# recommender = ExampleRecommender(n_examples=5, tokens="backrefs")
# recommender.fit(data)
# query, recommendations = recommender.predict(data, item_id=12)

# print(f"Query: {query}")
# print("Recommendations:")
# for recommendation in recommendations:
#     print(f"\t- {recommendation.split('/')[-1]}")
