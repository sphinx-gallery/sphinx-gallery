"""
Jupyterlite utility functions
=============================

Integration with Jupyterlite is on an experimental stage. Note that this API
may change in the future.
"""

import os
import shutil

from . import glr_path_static


def gen_jupyterlite_rst(fpath, gallery_conf):
    """Generate the RST + link for the Binder badge.

    Parameters
    ----------
    fpath: str
        The path to the `.ipynb` file for which a JupyterLite badge will be
        generated.

    gallery_conf : dict
        Sphinx-Gallery configuration dictionary.

    Returns
    -------
    rst : str
        The reStructuredText for the JupyterLite badge that links to this file.
    """
    relative_link = os.path.relpath(fpath, gallery_conf['src_dir'])
    notebook_location = relative_link.replace('.py', '.ipynb')
    lite_url = f"../lite/lab/index.html?path={notebook_location}"
    # Similar work-around for badge file as in
    # sphinx_gallery.binder.gen_binder_rst
    physical_path = os.path.join(
        os.path.dirname(fpath), 'images', 'jupyterlite_badge.svg')
    os.makedirs(os.path.dirname(physical_path), exist_ok=True)
    if not os.path.isfile(physical_path):
        shutil.copyfile(
            os.path.join(glr_path_static(), 'jupyterlite_badge.svg'),
            physical_path)
    rst = (
        "\n"
        "  .. container:: lite-badge\n\n"
        "    .. image:: images/jupyterlite_badge.svg\n"
        "      :target: {}\n"
        "      :alt: Launch JupyterLite\n"
        "      :width: 150 px\n").format(lite_url)
    return rst

