# -*- coding: utf-8 -*-
"""Recommendation system generator.

Generate recommendations based on TF-IDF representation and a KNN model.
"""
# Author: Arturo Amor
# License: 3-clause BSD


import numbers
import re
from collections import defaultdict
from pathlib import Path

from sphinx.errors import ConfigError
from .backreferences import (
    _thumbnail_div,
    THUMBNAIL_PARENT_DIV,
    THUMBNAIL_PARENT_DIV_CLOSE,
)
from .py_source_parser import split_code_and_text_blocks
from .gen_rst import extract_intro_and_title
from .utils import _replace_md5


class ExampleRecommender:
    """Compute content-based KNN-TF-IFD recommendation system.

    Parameters
    ----------
    n_examples : int, default=5
        Number of most relevant examples to display.
    min_df : float in range [0.0, 1.0] or int, default=1
        When building the vocabulary ignore terms that have a document frequency
        strictly lower than the given threshold. If float, the parameter
        represents a proportion of documents, integer represents absolute
        counts. This value is also called cut-off in the literature.
    max_df : float in range [0.0, 1.0] or int, default=1.0
        When building the vocabulary ignore terms that have a document frequency
        strictly higher than the given threshold. If float, the parameter
        represents a proportion of documents, integer represents absolute
        counts.

    Attributes
    ----------
    file_names_ : list of str
        The list of file names used for computing the similarity matrix.
        The recommended examples are chosen among this list.

    similarity_matrix_ : dense matrix
        Fitted matrix of pairwise cosine similarities.
    """

    def __init__(self, *, n_examples=5, min_df=3, max_df=0.9):
        self.n_examples = n_examples
        self.min_df = min_df
        self.max_df = max_df

    def token_freqs(self, doc):
        """Extract a dict mapping raw tokens from doc to their occurrences."""
        token_generator = (tok.lower() for tok in re.findall(r"\w+", doc))
        return self.dict_freqs(token_generator)

    @staticmethod
    def dict_freqs(doc):
        """Extract a dict mapping list of tokens to their occurrences."""
        freq = defaultdict(int)
        for tok in doc:
            freq[tok] += 1
        return freq

    def dict_vectorizer(self, data):
        """Convert a dictionary of feature arrays into a matrix.

        Parameters
        ----------
        data : list of dict
            An iterable of dictionaries of feature arrays, where each key
            corresponds to a feature name, and each value is an array of
            feature values.

        Returns
        -------
        X : ndarray of shape (n_samples, n_features)
            A matrix of occurrences where n_samples is the number of samples in
            the dataset and n_features is the total number of features across
            all samples.
        """
        try:
            import numpy as np

        except ImportError:
            raise ConfigError("gallery_conf['recommender'] requires numpy")

        feature_names = []
        all_values = defaultdict(list)
        for row in data:
            for feature_name, feature_value in row.items():
                feature_names.append(feature_name)
                all_values[feature_name].append(feature_value)

        feature_dict = {feature: i for i, feature in enumerate(sorted(all_values))}
        X = np.zeros((len(data), len(feature_dict)))
        for row_idx, row in enumerate(data):
            for feature_name, feature_value in row.items():
                X[row_idx, feature_dict[feature_name]] = feature_value
        return X

    def compute_tf_idf(self, X):
        """Transform a term frequency matrix into a TF-IDF matrix.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            A term frequency matrix.

        Returns
        -------
        X_tfidf : ndarray of shape (n_samples, n_features)
            A tf-idf matrix of the same shape as X.
        """
        import numpy as np

        n_samples = X.shape[0] + 1  # avoid taking log of 0

        df = np.count_nonzero(X, axis=0) + 1
        idf = np.log(n_samples / df) + 1
        X_tfidf = X * idf
        X_tfidf = (X_tfidf.T / np.linalg.norm(X_tfidf, axis=1)).T

        return X_tfidf

    def cosine_similarity(self, X, Y=None):
        """
        Compute the cosine similarity between two vectors X and Y.

        Parameters
        ----------
        X : ndarray of shape (n_samples_X, n_features)
            Input data.

        Y : ndarray of shape (n_samples_Y, n_features), default=None
            Input data. If `None`, the output will be the pairwise
            similarities between all samples in `X`.

        Returns
        -------
        cosine_similarity : ndarray of shape (n_samples_X, n_samples_Y)
            Cosine similarity matrix.
        """
        import numpy as np

        if Y is X or Y is None:
            Y = X

        X_normalized = X / np.linalg.norm(X)
        if X is Y:
            Y_normalized = X_normalized
        else:
            Y_normalized = Y / np.linalg.norm(Y)
        similarity = X_normalized @ Y_normalized.T

        return similarity

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
        import numpy as np

        n_examples = self.n_examples
        min_df = self.min_df
        max_df = self.max_df
        if not isinstance(n_examples, numbers.Integral):
            raise ValueError("n_examples must be an integer")
        elif n_examples < 1:
            raise ValueError("n_examples must be strictly positive")

        freq_func = self.token_freqs
        counts_matrix = self.dict_vectorizer(
            [freq_func(Path(fname).read_text()) for fname in file_names]
        )

        if isinstance(min_df, float) and 0.0 < min_df <= 1.0:
            min_df = int(np.ceil(min_df * counts_matrix.shape[0]))
        elif not isinstance(min_df, numbers.Integral) and min_df > 1:
            raise ValueError("min_df must be float in range [0.0, 1.0] or int")
        if isinstance(max_df, float) and 0.0 < max_df <= 1.0:
            max_df = int(np.floor(max_df * counts_matrix.shape[0]))
        elif not isinstance(max_df, numbers.Integral) and max_df > 1:
            raise ValueError("max_df must be float in range [0.0, 1.0] or int")
        doc_appearances = np.sum(counts_matrix, axis=0)
        mask = (doc_appearances >= min_df) & (doc_appearances <= max_df)
        self.similarity_matrix_ = self.cosine_similarity(
            self.compute_tf_idf(counts_matrix[:, mask])
        )
        self.file_names_ = file_names
        return self

    def predict(self, file_name):
        """Compute the `n_examples` most similar documents to the query.

        Parameters
        ----------
        file_name : str
            Name of the file corresponding to the query index `item_id`.

        Returns
        -------
        recommendations : list of str
            Name of the files most similar to the query.
        """
        item_id = self.file_names_.index(file_name)
        similar_items = list(enumerate(self.similarity_matrix_[item_id]))
        sorted_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

        # Get the top k items similar to item_id. Note that `sorted_items[0]`
        # is always the query document itself, hence it is discarded from the
        # returned list of recommendations.
        top_k_items = [idx for idx, _ in sorted_items[1 : self.n_examples + 1]]
        recommendations = [self.file_names_[idx] for idx in top_k_items]
        return recommendations


def _write_recommendations(recommender, fname, gallery_conf):
    """Generate `.recommendations` reST file for a given example.

    Parameters
    ----------
    recommender : ExampleRecommender
        Instance of a fitted ExampleRecommender.

    fname : str
        Path to the example file.

    gallery_conf : dict
        Configuration dictionary for the sphinx-gallery extension.
    """
    path_fname = Path(fname)
    recommend_fname = f"{path_fname.parent / path_fname.stem}.recommendations.new"
    recommended_examples = recommender.predict(fname)

    with open(recommend_fname, "w", encoding="utf-8") as ex_file:
        ex_file.write("\n\n.. rubric:: Related examples\n")
        ex_file.write(THUMBNAIL_PARENT_DIV)
        for example_fname in recommended_examples:
            example_path = Path(example_fname)
            _, script_blocks = split_code_and_text_blocks(
                example_fname, return_node=False
            )
            intro, title = extract_intro_and_title(fname, script_blocks[0][1])
            ex_file.write(
                _thumbnail_div(
                    example_path.parent,
                    gallery_conf["src_dir"],
                    example_path.name,
                    intro,
                    title,
                    is_backref=True,
                )
            )
        ex_file.write(THUMBNAIL_PARENT_DIV_CLOSE)
    _replace_md5(recommend_fname, mode="t")
