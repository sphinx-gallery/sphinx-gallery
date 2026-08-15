"""Pytest fixtures."""

import shutil
from contextlib import contextmanager
from io import StringIO
from pathlib import Path
from unittest.mock import Mock

import pytest
import sphinx
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx.util.docutils import docutils_namespace

from sphinx_gallery import docs_resolv, gen_gallery, gen_rst, py_source_parser
from sphinx_gallery.scrapers import _import_matplotlib


def pytest_report_header(config, startdir=None):
    """Add information to the pytest run header."""
    return f"Sphinx:  {sphinx.__version__} ({sphinx.__file__})"


@pytest.fixture
def gallery_conf(tmp_path):
    """Set up a test sphinx-gallery configuration."""
    app = Mock(
        spec=Sphinx,
        config=dict(source_suffix={".rst": None}, default_role=None),
        extensions=[],
    )
    gallery_conf = gen_gallery._fill_gallery_conf_defaults({}, app=app)
    gen_gallery._update_gallery_conf_builder_inited(gallery_conf, str(tmp_path))
    gallery_conf.update(examples_dir=str(tmp_path), gallery_dir=str(tmp_path))
    return gallery_conf


@pytest.fixture
def log_collector(monkeypatch):
    app = Mock(spec=Sphinx, name="FakeSphinxApp")()
    monkeypatch.setattr(docs_resolv, "logger", app)
    monkeypatch.setattr(gen_gallery, "logger", app)
    monkeypatch.setattr(py_source_parser, "logger", app)
    monkeypatch.setattr(gen_rst, "logger", app)
    yield app


@pytest.fixture
def unicode_sample(tmp_path):
    """Return temporary python source file with Unicode in various places."""
    code_str = b"""# -*- coding: utf-8 -*-
'''
\xc3\x9anicode in header
=================

U\xc3\xb1icode in description
'''

# Code source: \xc3\x93scar N\xc3\xa1jera
# License: BSD 3 clause

import os
path = os.path.join('a','b')

a = 'hei\xc3\x9f'  # Unicode string

import sphinx_gallery.back_references as br
br.identify_names

from sphinx_gallery.back_references import identify_names
identify_names

from sphinx_gallery._dummy import DummyClass
DummyClass().prop

from sphinx_gallery._dummy.nested import NestedDummyClass
NestedDummyClass().prop

import matplotlib.pyplot as plt
_ = plt.figure()

"""

    fname = tmp_path / "unicode_sample.py"
    fname.write_bytes(code_str)
    return fname


@pytest.fixture
def req_mpl_jpg(tmp_path, req_mpl, scope="session"):
    """Raise SkipTest if JPEG support is not available."""
    # mostly this is needed because of
    # https://github.com/matplotlib/matplotlib/issues/16083
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(range(10))
    try:
        plt.savefig(tmp_path / "testplot.jpg")
    except Exception as exp:
        pytest.skip(f"Matplotlib jpeg saving failed: {exp}")
    finally:
        plt.close(fig)


@pytest.fixture(scope="session")
def req_mpl():
    try:
        _import_matplotlib()
    except (ImportError, ValueError):
        pytest.skip("Test requires matplotlib")


@pytest.fixture(scope="session")
def req_pil():
    pytest.importorskip("PIL.Image")


@pytest.fixture
def conf_file(request):
    try:
        env = request.node.get_closest_marker("add_conf")
    except AttributeError:  # old pytest
        env = request.node.get_marker("add_conf")
    kwargs = env.kwargs if env else {}
    result = {
        "content": "",
        "extensions": ["sphinx_gallery.gen_gallery"],
    }
    result.update(kwargs)

    return result


@pytest.fixture
def rst_file(request):
    """Adds file(s) to environment, see `sphinx_app_wrapper` for details.

    This fixture takes a single `file` kwarg, which should be a dictionary
    of format {key: <file path>, value: <content to be added to file>}.
    The file path should be relative to the test documentation source path,
    see `sphinx_app_wrapper` for details.
    """
    env = request.node.get_closest_marker("add_file")
    file = env.kwargs["file"] if env else None
    return file


class SphinxAppWrapper:
    """Wrapper for sphinx.application.Application.

    This allows control over when the sphinx application is initialized, since
    part of the sphinx-gallery build is done in
    sphinx.application.Application.__init__ and the remainder is done in
    sphinx.application.Application.build.
    """

    def __init__(self, srcdir, confdir, outdir, doctreedir, buildername, **kwargs):
        self.srcdir = srcdir
        self.confdir = confdir
        self.outdir = outdir
        self.doctreedir = doctreedir
        self.buildername = buildername
        self.kwargs = kwargs

    def create_sphinx_app(self):
        """Create Sphinx app."""
        # Avoid warnings about re-registration, see:
        # https://github.com/sphinx-doc/sphinx/issues/5038
        with self.create_sphinx_app_context() as app:
            pass
        return app

    @contextmanager
    def create_sphinx_app_context(self):
        """Create Sphinx app inside context."""
        with docutils_namespace():
            app = Sphinx(
                self.srcdir,
                self.confdir,
                self.outdir,
                self.doctreedir,
                self.buildername,
                **self.kwargs,
            )
            yield app

    def build_sphinx_app(self, *args, **kwargs):
        """Build Sphinx app."""
        with self.create_sphinx_app_context() as app:
            # building should be done in the same docutils_namespace context
            app.build(*args, **kwargs)
        return app


@pytest.fixture
def sphinx_app_wrapper(tmp_path, conf_file, rst_file, req_mpl, req_pil):
    _fixturedir = Path(__file__).parent / "testconfs"
    srcdir = tmp_path / "config_test"
    shutil.copytree(_fixturedir, srcdir)
    # Copy files to 'examples/' as well because default `examples_dirs` is
    # '../examples' - for tests where we don't update config
    shutil.copytree(_fixturedir / "src", tmp_path / "examples")
    if rst_file:
        for file_name, content in rst_file.items():
            full_path = srcdir / file_name
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)

    base_config = f"""
import os
import sphinx_gallery
extensions = {conf_file["extensions"]!r}
exclude_patterns = ['_build', 'src']
source_suffix = '.rst'
master_doc = 'index'
# General information about the project.
project = 'Sphinx-Gallery <Tests>'\n\n
"""
    with open((srcdir / "conf.py"), "w") as conffile:
        conffile.write(base_config + conf_file["content"])

    return SphinxAppWrapper(
        srcdir,
        srcdir,
        (srcdir / "_build"),
        (srcdir / "_build" / "toctree"),
        "html",
        warning=StringIO(),
        status=StringIO(),
    )
