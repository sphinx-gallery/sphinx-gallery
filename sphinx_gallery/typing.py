"""
Typing definitions for Sphinx-Gallery.
"""

from typing import Any, TypeAlias

GalleryConfig: TypeAlias = dict[str, Any]
LinkType: TypeAlias = tuple[str | None, Any | None]
IntersphinxInventory: TypeAlias = dict[str, dict[str, Any]]
DocumentationOptions: TypeAlias = dict[str, str | int | bool]

Parser: TypeAlias = Any
"""
The type of the parser object used to parse source files.

TODO: This should become a protocol, but current implementations are inconsistent
and cannot be described with a single protocol:
- sphinx_gallery.py_source_parser (module)
- sphinx_gallery.rst_source_parser (module)
- sphinx_gallery.block_parser.BlockParser (class)
"""
