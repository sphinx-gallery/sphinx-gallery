# Author: Arturo Amor
# License: 3-clause BSD
"""Test the example recommender plugin."""

import codecs
import os
import os.path as op
import re
import shutil
from io import StringIO

import pytest

import sphinx_gallery.gen_rst as sg
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace
from sphinx_gallery.recommender import ExampleRecommender, _write_recommendations


@pytest.fixture(scope="module")
def sphinx_app(tmpdir_factory, req_mpl, req_pil):
    return _sphinx_app(tmpdir_factory, "html")


def _sphinx_app(tmpdir_factory, buildername):
    # Skip if numpy not installed
    pytest.importorskip("numpy")

    temp_dir = (tmpdir_factory.getbasetemp() / f"root_{buildername}").strpath
    src_dir = op.join(op.dirname(__file__), "tinybuild")

    def ignore(src, names):
        return ("_build", "gen_modules", "auto_examples")

    shutil.copytree(src_dir, temp_dir, ignore=ignore)
    # For testing iteration, you can get similar behavior just doing `make`
    # inside the tinybuild/doc directory
    conf_dir = op.join(temp_dir, "doc")
    out_dir = op.join(conf_dir, "_build", buildername)
    toctrees_dir = op.join(conf_dir, "_build", "toctrees")
    # Avoid warnings about re-registration, see:
    # https://github.com/sphinx-doc/sphinx/issues/5038
    with docutils_namespace():
        app = Sphinx(
            conf_dir,
            conf_dir,
            out_dir,
            toctrees_dir,
            buildername=buildername,
            status=StringIO(),
            warning=StringIO(),
        )
        # need to build within the context manager
        # for automodule and backrefs to work
        app.build(False, [])
    return app


def test_recommend_n_examples(sphinx_app):
    """Test exactly n_examples thumbnails are displayed in the tiny gallery."""
    pytest.importorskip("numpy")
    root = op.join(sphinx_app.outdir, "auto_examples")
    fname = op.join(root, "plot_defer_figures.html")
    with codecs.open(fname, "r", "utf-8") as fid:
        html = fid.read()

    count = html.count('<div class="sphx-glr-thumbnail-title">')
    n_examples = sphinx_app.config.sphinx_gallery_conf["recommender"]["n_examples"]

    assert '<p class="rubric">Related examples</p>' in html
    assert count == n_examples


def test_example_recommender_methods():
    """Test dict_vectorizer and compute_tf_idf methods."""
    np = pytest.importorskip("numpy")
    recommender = ExampleRecommender()
    D = [{"foo": 1, "bar": 2}, {"foo": 3, "baz": 1}]

    X = recommender.dict_vectorizer(D)
    expected_X = np.array([[2.0, 0.0, 1.0], [0.0, 1.0, 3.0]])
    np.testing.assert_array_equal(X, expected_X)

    X_tfidf = recommender.compute_tf_idf(X)
    expected_X_tfidf = np.array(
        [[0.94215562, 0.0, 0.33517574], [0.0, 0.42423963, 0.90554997]]
    )
    np.testing.assert_array_almost_equal(X_tfidf, expected_X_tfidf)


def test_recommendation_files(gallery_conf):
    """Test generated files and that recommendations are relevant."""
    pytest.importorskip("numpy")
    gallery_conf["recommender"].update(
        [("enable", True), ("rubric_header", "Custom header")]
    )
    file_dict = {
        "fox_jumps_dog.py": "The quick brown fox jumped over the lazy dog",
        "dog_sleeps.py": "The lazy dog slept all day",
        "fox_eats_dog_food.py": "The quick brown fox ate the lazy dog's food",
        "dog_jumps_fox.py": "The quick dog jumped over the lazy fox",
    }

    for file_name, content in file_dict.items():
        file_path = os.path.join(gallery_conf["gallery_dir"], file_name)
        with open(file_path, "w") as f:
            f.write(content)
        sg.save_rst_example("example_rst", file_path, 0, 0, gallery_conf)

        test_file = re.sub(r"\.py$", ".rst", file_path)
        recommendation_file = re.sub(r"\.py$", ".recommendations", file_name)
        with codecs.open(test_file) as f:
            rst = f.read()

        assert recommendation_file in rst

    py_files = [
        fname
        for fname in os.listdir(gallery_conf["gallery_dir"])
        if os.path.splitext(fname)[1] == ".py"
    ]
    gallery_py_files = [
        os.path.join(gallery_conf["gallery_dir"], fname) for fname in py_files
    ]
    recommender = ExampleRecommender(n_examples=1, min_df=1)
    recommender.fit(gallery_py_files)
    recommended_example = recommender.predict(file_path)  # dog_jumps_fox.py

    assert os.path.basename(recommended_example[0]) == "fox_jumps_dog.py"

    # _write_recommendations needs a thumbnail, we then create a blank png
    thumb_path = os.path.join(gallery_conf["gallery_dir"], "images/thumb")
    os.makedirs(thumb_path, exist_ok=True)
    png_file = "sphx_glr_fox_jumps_dog_thumb.png"
    png_file_path = os.path.join(thumb_path, png_file)
    with open(png_file_path, "wb") as f:
        b"\x89PNG\r\n\x1a\n"  # generic png file signature

    recommendation_file = re.sub(r"\.py$", ".recommendations", file_path)
    _write_recommendations(recommender, file_path, gallery_conf)
    with codecs.open(recommendation_file) as f:
        rst = f.read()
    assert ".. rubric:: Custom header" in rst
