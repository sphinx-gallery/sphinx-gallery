"""Utilities for building docs."""

from sphinx_gallery.notebook import add_code_cell, add_markdown_cell


def notebook_modification_function(notebook_content, notebook_filename):
    """Implement JupyterLite-specific modifications of notebooks."""
    notebook_content_str = str(notebook_content)
    warning_template = "\n".join(
        [
            "<div class='alert alert-{message_class}'>",
            "",
            "# JupyterLite warning",
            "",
            "{message}",
            "</div>",
        ]
    )

    if "pyvista_examples" in notebook_filename:
        message_class = "danger"
        message = (
            "PyVista is not packaged in Pyodide, this notebook is not "
            "expected to work inside JupyterLite"
        )
    elif "import plotly" in notebook_content_str:
        message_class = "danger"
        message = (
            "This notebook is not expected to work inside JupyterLite for now."
            " There seems to be some issues with Plotly, see "
            "[this]('https://github.com/jupyterlite/jupyterlite/pull/950') "
            "for more details."
        )
    else:
        message_class = "warning"
        message = (
            "JupyterLite integration in sphinx-gallery is beta "
            "and it may break in unexpected ways"
        )

    markdown = warning_template.format(message_class=message_class, message=message)

    dummy_notebook_content = {"cells": []}
    add_markdown_cell(dummy_notebook_content, markdown)

    code_lines = []

    if "seaborn" in notebook_content_str:
        code_lines.append("%pip install seaborn")

    if code_lines:
        code_lines = ["# JupyterLite-specific code"] + code_lines
        code = "\n".join(code_lines)
        add_code_cell(dummy_notebook_content, code)

    notebook_content["cells"] = (
        dummy_notebook_content["cells"] + notebook_content["cells"]
    )


def reset_others(gallery_conf, fname):
    """Reset plotting functions."""
    try:
        import pyvista
    except Exception:
        pass
    else:
        pyvista.OFF_SCREEN = True
        # Preferred plotting style for documentation
        pyvista.set_plot_theme("document")
        pyvista.global_theme.window_size = [1024, 768]
        pyvista.global_theme.font.size = 22
        pyvista.global_theme.font.label_size = 22
        pyvista.global_theme.font.title_size = 22
        pyvista.global_theme.return_cpos = False
        # necessary when building the sphinx gallery
        pyvista.BUILDING_GALLERY = True
        pyvista.set_jupyter_backend(None)
    try:
        import plotly.io
    except Exception:
        pass
    else:
        plotly.io.renderers.default = "sphinx_gallery"
