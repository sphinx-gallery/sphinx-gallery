"""
Typing definitions for Sphinx-Gallery.
"""

from typing import Any, TypeAlias

GalleryConfig: TypeAlias = dict[str, Any]
LinkType: TypeAlias = tuple[str | None, Any | None]
IntersphinxInventory: TypeAlias = dict[str, dict[str, Any]]
DocumentationOptions: TypeAlias = dict[str, str | int | bool]
