# -*- coding: utf-8 -*-
r"""
Utilities for downloadable items
================================

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import absolute_import, division, print_function

import os
import zipfile

from .source_parser import supported_extensions

CODE_DOWNLOAD = """
\n.. container:: sphx-glr-footer

\n  .. container:: sphx-glr-download

     :download:`Download Python source code: {0} <{0}>`\n

\n  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: {1} <{1}>`\n"""


CODE_DOWNLOAD_NO_NOTEBOOK = """
\n.. container:: sphx-glr-footer

\n  .. container:: sphx-glr-download

     :download:`Download {lang} source code: {0} <{0}>`\n"""


CODE_ZIP_DOWNLOAD = """
\n.. container:: sphx-glr-footer

\n  .. container:: sphx-glr-download

    :download:`Download all examples in Python source code: {0} </{1}>`\n

\n  .. container:: sphx-glr-download

    :download:`Download all examples in Jupyter notebooks: {2} </{3}>`\n"""


def ceate_zip(file_list, gallery_path, suffix='source'):
    """Store all files in file_list into an zip file.

    Parameters
    ----------
    file_list : list of strings
        Holds all the file names to be included in zip file
    gallery_path : string
        path to where the zipfile is stored
    sufffix : str
        In order to save with downloads of various sources/notebooks seperately
        you provide a suffix for the zip file saved.
    Returns
    -------
    zipname : string
        zip file name, written as `target_dir_{suffix}.zip`
        depending on the extension
    """
    zipname = gallery_path.replace(os.path.sep, '_')
    zipname += '_{}'.format(suffix)
    zipname = os.path.join(gallery_path, zipname + '.zip')

    zipf = zipfile.ZipFile(zipname, mode='w')
    for fname in file_list:
        zipf.write(fname)

    zipf.close()

    return zipname


def list_downloadable_sources(target_dir, extension=supported_extensions):
    """Return a list of all supported source files in target_dir.

    Parameters
    ----------
    target_dir : string
        path to the directory where source files are
    extension: string or tuple of strings
        An extension or tuple of extensions to be matched.
    Returns
    -------
    list
        list of paths to all matched source files in `target_dir`
    """
    return [os.path.join(target_dir, fname)
            for fname in os.listdir(target_dir)
            if fname.endswith(extension)]


def generate_zipfiles(gallery_dir):
    """Create zip file by scaniing gallery_dir.

    Collect all Python source files and Jupyter notebooks in
    gallery_dir and makes zipfiles of them.

    Parameters
    ----------
    gallery_dir : string
        path of the gallery to collect downloadable sources

    Return
    ------
    download_rst: string
        RestructuredText to include download buttons to the generated files
    """
    all_srces = list_downloadable_sources(gallery_dir, supported_extensions)
    jptr_ntbks = list_downloadable_sources(gallery_dir, '.ipynb')
    for directory in sorted(os.listdir(gallery_dir)):
        target_dir = os.path.join(gallery_dir, directory)
        if os.path.isdir(target_dir):
            all_srces.extend(list_downloadable_sources(target_dir,
                                                       supported_extensions))
            jptr_ntbks.extend(list_downloadable_sources(target_dir, '.ipynb'))

    src_zipfile = ceate_zip(all_srces, gallery_dir, 'source')
    ntbk_zipfile = ceate_zip(jptr_ntbks, gallery_dir, 'jupyter')

    dw_rst = CODE_ZIP_DOWNLOAD.format(os.path.basename(src_zipfile),
                                      src_zipfile,
                                      os.path.basename(ntbk_zipfile),
                                      ntbk_zipfile)
    return dw_rst
