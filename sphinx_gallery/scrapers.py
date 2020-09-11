# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Scrapers for embedding images
=============================

Collect images that have been produced by code blocks.

The only scrapers we support are Matplotlib and Mayavi, others should
live in modules that will support them (e.g., PyVista, Plotly).
"""

import os
import sys
import re
from distutils.version import LooseVersion
from textwrap import indent
from warnings import filterwarnings

from sphinx.errors import ExtensionError
from .utils import scale_image, optipng

__all__ = ['save_figures', 'figure_rst', 'ImagePathIterator', 'clean_modules',
           'matplotlib_scraper', 'mayavi_scraper']


###############################################################################
# Scrapers

def _import_matplotlib():
    """Import matplotlib safely."""
    # make sure that the Agg backend is set before importing any
    # matplotlib
    import matplotlib
    matplotlib.use('agg')
    matplotlib_backend = matplotlib.get_backend().lower()

    filterwarnings("ignore", category=UserWarning,
                   message='Matplotlib is currently using agg, which is a'
                           ' non-GUI backend, so cannot show the figure.')

    if matplotlib_backend != 'agg':
        raise ExtensionError(
            "Sphinx-Gallery relies on the matplotlib 'agg' backend to "
            "render figures and write them to files. You are "
            "currently using the {} backend. Sphinx-Gallery will "
            "terminate the build now, because changing backends is "
            "not well supported by matplotlib. We advise you to move "
            "sphinx_gallery imports before any matplotlib-dependent "
            "import. Moving sphinx_gallery imports at the top of "
            "your conf.py file should fix this issue"
            .format(matplotlib_backend))

    import matplotlib.pyplot as plt
    return matplotlib, plt


def _matplotlib_fig_titles(fig):
    titles = []
    # get supertitle if exists
    suptitle = getattr(fig, "_suptitle", None)
    if suptitle is not None:
        titles.append(suptitle.get_text())
    # get titles from all axes, for all locs
    title_locs = ['left', 'center', 'right']
    for ax in fig.axes:
        for loc in title_locs:
            text = ax.get_title(loc=loc)
            if text:
                titles.append(text)
    fig_titles = ', '.join(titles)
    return fig_titles


_ANIMATION_RST = '''
.. container:: sphx-glr-animation

    .. raw:: html

        {0}
'''


def matplotlib_scraper(block, block_vars, gallery_conf, **kwargs):
    """Scrape Matplotlib images.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    **kwargs : dict
        Additional keyword arguments to pass to
        :meth:`~matplotlib.figure.Figure.savefig`, e.g. ``format='svg'``.
        The ``format`` kwarg in particular is used to set the file extension
        of the output file (currently only 'png', 'jpg', and 'svg' are
        supported).

    Returns
    -------
    rst : str
        The ReSTructuredText that will be rendered to HTML containing
        the images. This is often produced by :func:`figure_rst`.
    """
    matplotlib, plt = _import_matplotlib()
    from matplotlib.animation import Animation
    image_path_iterator = block_vars['image_path_iterator']
    image_rsts = []
    # Check for animations
    anims = list()
    if gallery_conf.get('matplotlib_animations', False):
        for ani in block_vars['example_globals'].values():
            if isinstance(ani, Animation):
                anims.append(ani)
    # Then standard images
    for fig_num, image_path in zip(plt.get_fignums(), image_path_iterator):
        if 'format' in kwargs:
            image_path = '%s.%s' % (os.path.splitext(image_path)[0],
                                    kwargs['format'])
        # Set the fig_num figure as the current figure as we can't
        # save a figure that's not the current figure.
        fig = plt.figure(fig_num)
        # Deal with animations
        cont = False
        for anim in anims:
            if anim._fig is fig:
                image_rsts.append(_anim_rst(anim, image_path, gallery_conf))
                cont = True
                break
        if cont:
            continue
        # get fig titles
        fig_titles = _matplotlib_fig_titles(fig)
        to_rgba = matplotlib.colors.colorConverter.to_rgba
        # shallow copy should be fine here, just want to avoid changing
        # "kwargs" for subsequent figures processed by the loop
        these_kwargs = kwargs.copy()
        for attr in ['facecolor', 'edgecolor']:
            fig_attr = getattr(fig, 'get_' + attr)()
            default_attr = matplotlib.rcParams['figure.' + attr]
            if to_rgba(fig_attr) != to_rgba(default_attr) and \
                    attr not in kwargs:
                these_kwargs[attr] = fig_attr
        try:
            fig.savefig(image_path, **these_kwargs)
        except Exception:
            plt.close('all')
            raise
        if 'images' in gallery_conf['compress_images']:
            optipng(image_path, gallery_conf['compress_images_args'])
        image_rsts.append(
            figure_rst([image_path], gallery_conf['src_dir'], fig_titles))
    plt.close('all')
    rst = ''
    if len(image_rsts) == 1:
        rst = image_rsts[0]
    elif len(image_rsts) > 1:
        image_rsts = [re.sub(r':class: sphx-glr-single-img',
                             ':class: sphx-glr-multi-img',
                             image) for image in image_rsts]
        image_rsts = [HLIST_IMAGE_MATPLOTLIB + indent(image, u' ' * 6)
                      for image in image_rsts]
        rst = HLIST_HEADER + ''.join(image_rsts)
    return rst


def _anim_rst(anim, image_path, gallery_conf):
    import matplotlib
    from matplotlib.animation import FFMpegWriter, ImageMagickWriter
    # output the thumbnail as the image, as it will just be copied
    # if it's the file thumbnail
    fig = anim._fig
    image_path = image_path.replace('.png', '.gif')
    fig_size = fig.get_size_inches()
    thumb_size = gallery_conf['thumbnail_size']
    use_dpi = round(
        min(t_s / f_s for t_s, f_s in zip(thumb_size, fig_size)))
    # FFmpeg is buggy for GIFs before Matplotlib 3.3.1
    if LooseVersion(matplotlib.__version__) >= LooseVersion('3.3.1') and \
            FFMpegWriter.isAvailable():
        writer = 'ffmpeg'
    elif ImageMagickWriter.isAvailable():
        writer = 'imagemagick'
    else:
        writer = None
    anim.save(image_path, writer=writer, dpi=use_dpi)
    html = anim._repr_html_()
    if html is None:  # plt.rcParams['animation.html'] == 'none'
        html = anim.to_jshtml()
    html = indent(html, '     ')
    return _ANIMATION_RST.format(html)


def mayavi_scraper(block, block_vars, gallery_conf):
    """Scrape Mayavi images.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    rst : str
        The ReSTructuredText that will be rendered to HTML containing
        the images. This is often produced by :func:`figure_rst`.
    """
    from mayavi import mlab
    image_path_iterator = block_vars['image_path_iterator']
    image_paths = list()
    e = mlab.get_engine()
    for scene, image_path in zip(e.scenes, image_path_iterator):
        try:
            mlab.savefig(image_path, figure=scene)
        except Exception:
            mlab.close(all=True)
            raise
        # make sure the image is not too large
        scale_image(image_path, image_path, 850, 999)
        if 'images' in gallery_conf['compress_images']:
            optipng(image_path, gallery_conf['compress_images_args'])
        image_paths.append(image_path)
    mlab.close(all=True)
    return figure_rst(image_paths, gallery_conf['src_dir'])


_scraper_dict = dict(
    matplotlib=matplotlib_scraper,
    mayavi=mayavi_scraper,
)


class ImagePathIterator(object):
    """Iterate over image paths for a given example.

    Parameters
    ----------
    image_path : str
        The template image path.
    """

    def __init__(self, image_path):
        self.image_path = image_path
        self.paths = list()
        self._stop = 1000000

    def __len__(self):
        """Return the number of image paths used.

        Returns
        -------
        n_paths : int
            The number of paths.
        """
        return len(self.paths)

    def __iter__(self):
        """Iterate over paths.

        Returns
        -------
        paths : iterable of str

        This enables the use of this Python pattern::

            >>> for epoch in epochs:  # doctest: +SKIP
            >>>     print(epoch)  # doctest: +SKIP

        Where ``epoch`` is given by successive outputs of
        :func:`mne.Epochs.next`.
        """
        # we should really never have 1e6, let's prevent some user pain
        for ii in range(self._stop):
            yield self.next()
        else:
            raise ExtensionError('Generated over %s images' % (self._stop,))

    def next(self):
        return self.__next__()

    def __next__(self):
        # The +1 here is because we start image numbering at 1 in filenames
        path = self.image_path.format(len(self) + 1)
        self.paths.append(path)
        return path


# For now, these are what we support
_KNOWN_IMG_EXTS = ('png', 'svg', 'jpg', 'gif')


def _find_image_ext(path):
    """Find an image, tolerant of different file extensions."""
    path = os.path.splitext(path)[0]
    for ext in _KNOWN_IMG_EXTS:
        this_path = '%s.%s' % (path, ext)
        if os.path.isfile(this_path):
            break
    else:
        ext = 'png'
    return ('%s.%s' % (path, ext), ext)


def save_figures(block, block_vars, gallery_conf):
    """Save all open figures of the example code-block.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document.
    """
    image_path_iterator = block_vars['image_path_iterator']
    all_rst = u''
    prev_count = len(image_path_iterator)
    for scraper in gallery_conf['image_scrapers']:
        rst = scraper(block, block_vars, gallery_conf)
        if not isinstance(rst, str):
            raise ExtensionError('rst from scraper %r was not a string, '
                                 'got type %s:\n%r'
                                 % (scraper, type(rst), rst))
        n_new = len(image_path_iterator) - prev_count
        for ii in range(n_new):
            current_path, _ = _find_image_ext(
                image_path_iterator.paths[prev_count + ii])
            if not os.path.isfile(current_path):
                raise ExtensionError(
                    'Scraper %s did not produce expected image:'
                    '\n%s' % (scraper, current_path))
        all_rst += rst
    return all_rst


def figure_rst(figure_list, sources_dir, fig_titles=''):
    """Generate RST for a list of image filenames.

    Depending on whether we have one or more figures, we use a
    single rst call to 'image' or a horizontal list.

    Parameters
    ----------
    figure_list : list
        List of strings of the figures' absolute paths.
    sources_dir : str
        absolute path of Sphinx documentation sources
    fig_titles : str
        Titles of figures, empty string if no titles found. Currently
        only supported for matplotlib figures, default = ''.

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    """

    figure_paths = [os.path.relpath(figure_path, sources_dir)
                    .replace(os.sep, '/').lstrip('/')
                    for figure_path in figure_list]
    # Get alt text
    alt = ''
    if fig_titles:
        alt = fig_titles
    elif figure_list:
        file_name = os.path.split(figure_list[0])[1]
        # remove ext & 'sphx_glr_' from start & n#'s from end
        file_name_noext = os.path.splitext(file_name)[0][9:-4]
        # replace - & _ with \s
        file_name_final = re.sub(r'[-,_]', ' ', file_name_noext)
        alt = file_name_final
    alt = _single_line_sanitize(alt)

    images_rst = ""
    if len(figure_paths) == 1:
        figure_name = figure_paths[0]
        images_rst = SINGLE_IMAGE % (figure_name, alt)
    elif len(figure_paths) > 1:
        images_rst = HLIST_HEADER
        for figure_name in figure_paths:
            images_rst += HLIST_IMAGE_TEMPLATE % (figure_name, alt)
    return images_rst


def _single_line_sanitize(s):
    """Remove problematic newlines."""
    # For example, when setting a :alt: for an image, it shouldn't have \n
    # This is a function in case we end up finding other things to replace
    return s.replace('\n', ' ')


# The following strings are used when we have several pictures: we use
# an html div tag that our CSS uses to turn the lists into horizontal
# lists.
HLIST_HEADER = """
.. rst-class:: sphx-glr-horizontal

"""

HLIST_IMAGE_MATPLOTLIB = """
    *
"""

HLIST_IMAGE_TEMPLATE = """
    *

      .. image:: /%s
          :alt: %s
          :class: sphx-glr-multi-img
"""

SINGLE_IMAGE = """
.. image:: /%s
    :alt: %s
    :class: sphx-glr-single-img
"""


###############################################################################
# Module resetting

def _reset_matplotlib(gallery_conf, fname):
    """Reset matplotlib."""
    _, plt = _import_matplotlib()
    plt.rcdefaults()


def _reset_seaborn(gallery_conf, fname):
    """Reset seaborn."""
    # Horrible code to 'unload' seaborn, so that it resets
    # its default when is load
    # Python does not support unloading of modules
    # https://bugs.python.org/issue9072
    for module in list(sys.modules.keys()):
        if 'seaborn' in module:
            del sys.modules[module]


_reset_dict = {
    'matplotlib': _reset_matplotlib,
    'seaborn': _reset_seaborn,
}


def clean_modules(gallery_conf, fname):
    """Remove, unload, or reset modules after running each example.

    After a script is executed it can load a variety of settings that one
    does not want to influence in other examples in the gallery.

    Parameters
    ----------
    gallery_conf : dict
        The gallery configuration.
    fname : str or None
        The example being run. Will be None when this is called entering
        a directory of examples to be built.
    """
    for reset_module in gallery_conf['reset_modules']:
        reset_module(gallery_conf, fname)
