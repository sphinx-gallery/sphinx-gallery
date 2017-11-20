import shutil as sh
import os
from copy import deepcopy

try:
    basestring
except NameError:
    basestring = str
    unicode = str

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
        A URL that can be used to direct the user to the live Binder environment.
    """
    # Build the URL
    binder_fpath = '_downloads/{}'.format(fname.replace('.py', '.ipynb'))
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

        'url': The URL of the BinderHub instance that's running a Binder service.
        'org': The GitHub organization to which the documentation will be pushed.
        'repo': The GitHub repository to which the documentation will be pushed.
        'branch': The Git branch on which the documentation exists (e.g., gh-pages).
        'dependencies': A list of paths to dependency files that match the Binder spec.

    Returns
    -------
    rst : str
        The reStructuredText for the Binder badge that links to this file.
    """
    binder_url = gen_binder_url(fname, binder_conf)
    rst = ".. figure:: http://mybinder.org/badge.svg\n      :target: {}\n".format(binder_url)
    rst += "      :width: 150 px\n      :figclass: binder-badge\n\n"
    return rst


def copy_binder_reqs(app):
    """Copy Binder requirements files to a "binder" folder in the docs."""
    binder_conf = app.config.sphinx_gallery_conf.get('binder')
    path_reqs = binder_conf.get('dependencies', None)
    if not isinstance(path_reqs, (list, tuple)):
        path_reqs = [path_reqs]

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
    missing_values = []
    for val in req_values:
        if not isinstance(binder_conf.get(val, None), (str, unicode)):
            missing_values.append(val)

    if len(missing_values) > 0:
        raise ValueError('binder_conf is missing values for: {}'.format(
            missing_values))

    # Ensure we have http in the URL
    if not any(binder_conf['url'].startswith(ii)
               for ii in ['http://', 'https://']):
        raise ValueError('did not supply a valid url, '
                         'gave url: {}'.format(binder_conf['url']))

    # Ensure we have at least one dependency file
    # Need at least one of these two files
    required_reqs_files = ['requirements.txt', 'environment.yml']
    path_reqs = binder_conf['dependencies']
    if not isinstance(path_reqs, list):
        path_reqs = [path_reqs]

    if not any(ireq.endswith(ii)
               for ii in required_reqs_files for ireq in path_reqs):
        raise ValueError('Must provide requirements path to at least one of '
                         '{}'.format(required_reqs_files))
    return binder_conf
