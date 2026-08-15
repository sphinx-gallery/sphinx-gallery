"""Helper functions for testing, such as custom sorters for examples and subsections.

The data and functions here are used in test_gen_gallery.py to test the custom sorting
functionality. They are defined in a submodule of sphinx_gallery and not in the test
code itself, because they must be easily accessible via their fully qualified name as
string.
"""

from pathlib import Path

CUSTOM_EXAMPLE_ORDER = [
    "plot_1.py",
    "plot_3.py",
    "plot_2.py",
    "plot_5.py",
    "plot_6.py",
    "plot_4.py",
    "plot_8.py",
    "plot_7.py",
    "plot_9.py",
]


def custom_example_sorter(filename: str) -> int:
    """Importable custom sorter func, used in our test suite."""
    return CUSTOM_EXAMPLE_ORDER.index(filename)


def custom_subsection_sorter(foldername: str) -> str:
    """Importable custom sorter func for subsection folders, used in our test suite."""
    return foldername[::-1]


def custom_minigallery_sort_order_sorter(file: str) -> int:
    """Importable custom sorter for minigallery_sort_order, used in our test suite."""
    ORDER = [
        "plot_3.py",
        "plot_2.py",
        "plot_1.py",
    ]
    return ORDER.index(Path(file).name)
