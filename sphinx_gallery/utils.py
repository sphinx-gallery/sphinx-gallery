# -*- coding: utf-8 -*-
"""
Utilities
=========

Miscellaneous utilities.
"""
# Author: Eric Larson
# License: 3-clause BSD

from __future__ import division, absolute_import, print_function

import hashlib
import os
from shutil import move, copyfile


def _get_image():
    try:
        from PIL import Image
    except ImportError as exc:  # capture the error for the modern way
        try:
            import Image
        except ImportError:
            raise RuntimeError('Could not import pillow, which is required '
                               'to rescale images (e.g., for thumbnails): %s'
                               % (exc,))
    return Image


def scale_image(in_fname, out_fname, max_width, max_height):
    """Scales an image with the same aspect ratio centered in an
       image box with the given max_width and max_height
       if in_fname == out_fname the image can only be scaled down
    """
    # local import to avoid testing dependency on PIL:
    Image = _get_image()
    img = Image.open(in_fname)
    width_in, height_in = img.size
    scale_w = max_width / float(width_in)
    scale_h = max_height / float(height_in)

    if height_in * scale_w <= max_height:
        scale = scale_w
    else:
        scale = scale_h

    if scale >= 1.0 and in_fname == out_fname:
        return

    width_sc = int(round(scale * width_in))
    height_sc = int(round(scale * height_in))

    # resize the image using resize; if using .thumbnail and the image is
    # already smaller than max_width, max_height, then this won't scale up
    # at all (maybe could be an option someday...)
    img = img.resize((width_sc, height_sc), Image.BICUBIC)
    # img.thumbnail((width_sc, height_sc), Image.BICUBIC)
    # width_sc, height_sc = img.size  # necessary if using thumbnail

    # insert centered
    thumb = Image.new('RGBA', (max_width, max_height), (255, 255, 255, 255))
    pos_insert = ((max_width - width_sc) // 2, (max_height - height_sc) // 2)
    thumb.paste(img, pos_insert)

    try:
        thumb.save(out_fname)
    except IOError:
        # try again, without the alpha channel (e.g., for JPEG)
        thumb.convert('RGB').save(out_fname)


def replace_py_ipynb(fname):
    """Replace .py extension in filename by .ipynb"""
    fname_prefix, extension = os.path.splitext(fname)
    allowed_extension = '.py'
    if extension != allowed_extension:
        raise ValueError(
            "Unrecognized file extension, expected %s, got %s"
            % (allowed_extension, extension))
    new_extension = '.ipynb'
    return '{}{}'.format(fname_prefix, new_extension)


def get_md5sum(src_file):
    """Returns md5sum of file"""
    with open(src_file, 'rb') as src_data:
        src_content = src_data.read()
        return hashlib.md5(src_content).hexdigest()


def _replace_md5(fname_new, fname_old=None, method='move'):
    assert method in ('move', 'copy')
    if fname_old is None:
        assert fname_new.endswith('.new')
        fname_old = os.path.splitext(fname_new)[0]
    if os.path.isfile(fname_old) and (get_md5sum(fname_old) ==
                                      get_md5sum(fname_new)):
        if method == 'move':
            os.remove(fname_new)
    else:
        if method == 'move':
            move(fname_new, fname_old)
        else:
            copyfile(fname_new, fname_old)
    assert os.path.isfile(fname_old)


class Bunch(dict):
    """Dictionary-like object that exposes its keys as attributes."""

    def __init__(self, **kwargs):  # noqa: D102
        dict.__init__(self, kwargs)
        self.__dict__ = self
