"""Testing sphinx_gallery.load_style extension."""

from pathlib import Path

import pytest


@pytest.mark.add_conf(extensions=["sphinx_gallery.load_style"])
def test_load_style(sphinx_app_wrapper):
    """Testing that style loads properly."""
    sphinx_app = sphinx_app_wrapper.build_sphinx_app()
    cfg = sphinx_app.config
    assert cfg.project == "Sphinx-Gallery <Tests>"
    build_warn = sphinx_app._warning.getvalue()
    assert build_warn == ""
    index_html = Path(sphinx_app_wrapper.outdir, "index.html")
    assert index_html.is_file()
    content = index_html.read_text()
    assert (
        'link rel="stylesheet" type="text/css" href="_static/sg_gallery.css' in content
    )
