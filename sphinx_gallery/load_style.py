"""Only load CSS and modify html_static_path.

This should not be used at the same time as sphinx_gallery.gen_gallery.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import __version__, glr_path_static
from .directives import ImageSg, imagesg_addnode

if TYPE_CHECKING:
    import sphinx.application
    import sphinx.config


def config_inited(
    app: sphinx.application.Sphinx,
    config: sphinx.config.Config,
) -> None:
    """Append path to packaged static files to `html_static_path`."""
    path = glr_path_static()
    if path not in config.html_static_path:
        config.html_static_path.append(path)
    app.add_css_file("sg_gallery.css")


def setup(app: sphinx.application.Sphinx) -> dict[str, object]:
    """Sphinx setup."""
    app.require_sphinx("1.8")
    app.connect("config-inited", config_inited)
    app.add_directive("image-sg", ImageSg)
    imagesg_addnode(app)
    return {
        "parallel_read_safe": True,
        "version": __version__,
    }
