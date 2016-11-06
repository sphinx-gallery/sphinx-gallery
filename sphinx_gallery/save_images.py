# -*- coding: utf-8 -*-
r"""
Save all figures from the execution of code blocks
==================================================

"""
# Author: Óscar Nájera
# License: 3-clause BSD

from __future__ import absolute_import, division, print_function

import os
import subprocess
import warnings

import matplotlib
import matplotlib.pyplot as plt


def save_matplotlib_figures(image_path, fig_count):
    figure_list = []

    for fig_num in plt.get_fignums():
        # Set the fig_num figure as the current figure as we can't
        # save a figure that's not the current figure.
        fig = plt.figure(fig_num)
        kwargs = {}
        to_rgba = matplotlib.colors.colorConverter.to_rgba
        for attr in ['facecolor', 'edgecolor']:
            fig_attr = getattr(fig, 'get_' + attr)()
            default_attr = matplotlib.rcParams['figure.' + attr]
            if to_rgba(fig_attr) != to_rgba(default_attr):
                kwargs[attr] = fig_attr

        current_fig = image_path.format(fig_count + fig_num)
        fig.savefig(current_fig, **kwargs)
        figure_list.append(current_fig)

    return figure_list


def save_mayavi_figures(image_path, fig_count):
    figure_list = []
    from mayavi import mlab
    e = mlab.get_engine()
    total_fig_num = fig_count + len(e.scenes)
    mayavi_fig_nums = range(fig_count + 1, total_fig_num + 1)

    for scene, mayavi_fig_num in zip(e.scenes, mayavi_fig_nums):
        current_fig = image_path.format(mayavi_fig_num)
        mlab.savefig(current_fig, figure=scene)
        # make sure the image is not too large
        scale_image(current_fig, current_fig, 850, 999)
        figure_list.append(current_fig)
    mlab.close(all=True)

    return figure_list


def scale_image(in_fname, out_fname, max_width, max_height):
    """Scales an image with the same aspect ratio centered in an
       image with a given max_width and max_height
       if in_fname == out_fname the image can only be scaled down
    """
    # local import to avoid testing dependency on PIL:
    try:
        from PIL import Image
    except ImportError:
        import Image
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

    # resize the image
    img.thumbnail((width_sc, height_sc), Image.ANTIALIAS)

    # insert centered
    thumb = Image.new('RGB', (max_width, max_height), (255, 255, 255))
    pos_insert = ((max_width - width_sc) // 2, (max_height - height_sc) // 2)
    thumb.paste(img, pos_insert)

    thumb.save(out_fname)
    # Use optipng to perform lossless compression on the resized image if
    # software is installed
    if os.environ.get('SKLEARN_DOC_OPTIPNG', False):
        try:
            subprocess.call(["optipng", "-quiet", "-o", "9", out_fname])
        except Exception:
            warnings.warn('Install optipng to reduce the size of the \
                          generated images')


def save_figures(image_path, fig_count, gallery_conf):
    """Save all open matplotlib figures of the example code-block

    Parameters
    ----------
    image_path : str
        Path where plots are saved (format string which accepts figure number)
    fig_count : int
        Previous figure number count. Figure number add from this number
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    figure_list : list of str
        strings containing the relative path to each figure
    images_rst : str
        rst code to embed the images in the document
    """
    figure_list = save_matplotlib_figures(image_path, fig_count)

    if gallery_conf.get('find_mayavi_figures', False):
        fig_count += len(figure_list)
        figure_list += save_mayavi_figures(image_path, fig_count)

    figure_list = [os.path.relpath(figure_path, gallery_conf['src_dir'])
                   for figure_path in figure_list]
    return figure_list
