# -*- coding: utf-8 -*-
# Author: Chris Holdgraf
# License: 3-clause BSD
"""
Binder utility functions
========================

Integration with Binder is on an experimental stage. Note that this API may
change in the future.

.. warning::

   Binder is still beta technology, so there may be instability in the
   experience of users who click Binder links.

"""

import shutil as sh
import os

try:
    basestring
except NameError:
    basestring = str
    unicode = str

from .utils import replace_py_ipynb


def gen_binder_url(fname, binder_conf):
    """Generate a Binder URL according to the configuration in conf.py.

    Parameters
    ----------
    fname: str
        The path to the `.py` file for which a Binder badge will be generated.
    binder_conf: dict | None
        The Binder configuration dictionary. See `gen_binder_rst` for details.

    Returns
    -------
    binder_url : str
        A URL that can be used to direct the user to the live Binder
        environment.
    """
    # Build the URL
    fpath_prefix = binder_conf.get('filepath_prefix')
    binder_fpath = '_downloads/{}'.format(replace_py_ipynb(fname))
    if fpath_prefix is not None:
        binder_fpath = '/'.join([fpath_prefix.strip('/'), binder_fpath])
    binder_url = binder_conf['url']
    binder_url = '/'.join([binder_conf['url'],
                           'v2', 'gh',
                           binder_conf['org'],
                           binder_conf['repo'],
                           binder_conf['branch']])
    binder_url += '?filepath={}'.format(binder_fpath)
    return binder_url


def gen_binder_rst(fname, binder_conf):
    """Generate the RST + link for the Binder badge.

    Parameters
    ----------
    fname: str
        The path to the `.py` file for which a Binder badge will be generated.
    binder_conf: dict | None
        If a dictionary it must have the following keys:

        'url': The URL of the BinderHub instance that's running a Binder
            service.
        'org': The GitHub organization to which the documentation will be
            pushed.
        'repo': The GitHub repository to which the documentation will be
            pushed.
        'branch': The Git branch on which the documentation exists (e.g.,
            gh-pages).
        'dependencies': A list of paths to dependency files that match the
            Binderspec.

    Returns
    -------
    rst : str
        The reStructuredText for the Binder badge that links to this file.
    """
    binder_url = gen_binder_url(fname, binder_conf)

    rst = (
        "\n"
        "  .. container:: binder-badge\n\n"
        "    .. image:: https://static.mybinder.org/badge.svg\n"
        "      :target: {}\n"
        "      :width: 150 px\n").format(binder_url)
    return rst


def copy_binder_reqs(app):
    """Copy Binder requirements files to a "binder" folder in the docs."""
    binder_conf = app.config.sphinx_gallery_conf['binder']
    path_reqs = binder_conf.get('dependencies')

    binder_folder = os.path.join(app.builder.outdir, 'binder')
    if not os.path.isdir(binder_folder):
        os.makedirs(binder_folder)
    for path in path_reqs:
        sh.copy(os.path.join(app.builder.srcdir, path),
                binder_folder)


def check_binder_conf(binder_conf):
    """Check to make sure that the Binder configuration is correct."""
    # Grab the configuration and return None if it's not configured
    binder_conf = {} if binder_conf is None else binder_conf
    if not isinstance(binder_conf, dict):
        raise ValueError('`binder_conf` must be a dictionary or None.')
    if len(binder_conf) == 0:
        return binder_conf

    # Ensure all fields are populated
    req_values = ['url', 'org', 'repo', 'branch', 'dependencies']
    optional_values = ['filepath_prefix']
    missing_values = []
    for val in req_values:
        if binder_conf.get(val) is None:
            missing_values.append(val)

    if len(missing_values) > 0:
        raise ValueError('binder_conf is missing values for: {}'.format(
            missing_values))

    for key in binder_conf.keys():
        if key not in (req_values + optional_values):
            raise ValueError("Unknown Binder config key: {}".format(key))

    # Ensure we have http in the URL
    if not any(binder_conf['url'].startswith(ii)
               for ii in ['http://', 'https://']):
        raise ValueError('did not supply a valid url, '
                         'gave url: {}'.format(binder_conf['url']))

    # Ensure we have at least one dependency file
    # Need at least one of these two files
    required_reqs_files = ['requirements.txt', 'environment.yml']
    path_reqs = binder_conf['dependencies']
    if isinstance(path_reqs, basestring):
        path_reqs = [path_reqs]
        binder_conf['dependencies'] = path_reqs
    elif not isinstance(path_reqs, (list, tuple)):
        raise ValueError("`dependencies` value should be a list of strings. "
                         "Got type {}.".format(type(path_reqs)))

    path_reqs_filenames = [os.path.basename(ii) for ii in path_reqs]
    if not any(ii in path_reqs_filenames for ii in required_reqs_files):
        raise ValueError(
            'Did not find one of `requirements.txt` or `environment.yml` '
            'in the "dependencies" section of the binder configuration '
            'for sphinx-gallery. A path to at least one of these files '
            'must exist in your Binder dependencies.')
    return binder_conf
