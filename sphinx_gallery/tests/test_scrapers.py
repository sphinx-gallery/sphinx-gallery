import os

import pytest
import numpy as np
from PIL import Image

from sphinx_gallery.gen_gallery import _complete_gallery_conf
from sphinx_gallery.scrapers import (figure_rst, mayavi_scraper, SINGLE_IMAGE,
                                     matplotlib_scraper, ImagePathIterator,
                                     save_figures)
from sphinx_gallery.utils import _TempDir


@pytest.fixture
def gallery_conf(tmpdir):
    """Sets up a test sphinx-gallery configuration"""
    gallery_conf = _complete_gallery_conf({}, str(tmpdir), True, False)
    gallery_conf.update(examples_dir=_TempDir(), gallery_dir=str(tmpdir))
    return gallery_conf


def test_save_matplotlib_figures(gallery_conf):
    """Test matplotlib figure save"""
    import matplotlib.pyplot as plt  # nest these so that Agg can be set
    plt.plot(1, 1)
    fname_template = os.path.join(gallery_conf['gallery_dir'], 'image{0}.png')
    image_path_iterator = ImagePathIterator(fname_template)
    block = ('',) * 3
    block_vars = dict(image_path_iterator=image_path_iterator)
    image_rst = save_figures(block, block_vars, gallery_conf)
    assert len(image_path_iterator) == 1
    assert '/image1.png' in image_rst

    # Test capturing 2 images with shifted start number
    image_path_iterator.next()
    image_path_iterator.next()
    plt.plot(1, 1)
    plt.figure()
    plt.plot(1, 1)
    image_rst = save_figures(block, block_vars, gallery_conf)
    assert len(image_path_iterator) == 5
    assert '/image4.png' in image_rst
    assert '/image5.png' in image_rst


def test_save_mayavi_figures(gallery_conf):
    """Test file naming when saving figures. Requires mayavi."""
    try:
        from mayavi import mlab
    except ImportError:
        raise pytest.skip('Mayavi not installed')
    import matplotlib.pyplot as plt
    mlab.options.offscreen = True

    gallery_conf.update(
        image_scrapers=(matplotlib_scraper, mayavi_scraper))
    fname_template = os.path.join(gallery_conf['gallery_dir'], 'image{0}.png')
    image_path_iterator = ImagePathIterator(fname_template)
    block = ('',) * 3
    block_vars = dict(image_path_iterator=image_path_iterator)

    plt.axes([-0.1, -0.1, 1.2, 1.2])
    plt.pcolor([[0]], cmap='Greens')
    mlab.test_plot3d()
    image_rst = save_figures(block, block_vars, gallery_conf)
    assert len(plt.get_fignums()) == 0
    assert len(image_path_iterator) == 2
    assert '/image0.png' not in image_rst
    assert '/image1.png' in image_rst
    assert '/image2.png' in image_rst
    assert '/image3.png' not in image_rst
    assert not os.path.isfile(fname_template.format(0))
    assert os.path.isfile(fname_template.format(1))
    assert os.path.isfile(fname_template.format(2))
    assert not os.path.isfile(fname_template.format(0))
    with Image.open(fname_template.format(1)) as img:
        pixels = np.asarray(img.convert("RGB"))
    assert (pixels == [247, 252, 245]).all()  # plt first

    # Test next-value handling, plus image_scrapers modification
    gallery_conf.update(image_scrapers=(matplotlib_scraper,))
    mlab.test_plot3d()
    plt.axes([-0.1, -0.1, 1.2, 1.2])
    plt.pcolor([[0]], cmap='Reds')
    image_rst = save_figures(block, block_vars, gallery_conf)
    assert len(plt.get_fignums()) == 0
    assert len(image_path_iterator) == 3
    assert '/image1.png' not in image_rst
    assert '/image2.png' not in image_rst
    assert '/image3.png' in image_rst
    assert '/image4.png' not in image_rst
    assert not os.path.isfile(fname_template.format(0))
    for ii in range(3):
        assert os.path.isfile(fname_template.format(ii + 1))
    assert not os.path.isfile(fname_template.format(4))
    with Image.open(fname_template.format(3)) as img:
        pixels = np.asarray(img.convert("RGB"))
    assert (pixels == [255, 245, 240]).all()

    # custom finders
    gallery_conf.update(image_scrapers=[lambda x, y, z: ''])
    image_rst = save_figures(block, block_vars, gallery_conf)
    assert len(image_path_iterator) == 3

    # degenerate
    gallery_conf.update(image_scrapers=['foo'])
    with pytest.raises(ValueError, match='Unknown image scraper'):
        _complete_gallery_conf(
            gallery_conf, gallery_conf['gallery_dir'], True, False)
    gallery_conf.update(
        image_scrapers=[lambda x, y, z: y['image_path_iterator'].next()])
    with pytest.raises(RuntimeError, match='did not produce expected image'):
        save_figures(block, block_vars, gallery_conf)
    gallery_conf.update(image_scrapers=[lambda x, y, z: 1.])
    with pytest.raises(TypeError, match='was not a string'):
        save_figures(block, block_vars, gallery_conf)


def test_figure_rst():
    """Testing rst of images"""
    figure_list = ['sphx_glr_plot_1.png']
    image_rst = figure_rst(figure_list, '.')
    single_image = """
.. image:: /sphx_glr_plot_1.png
    :class: sphx-glr-single-img
"""
    assert image_rst == single_image

    image_rst = figure_rst(figure_list + ['second.png'], '.')

    image_list_rst = """
.. rst-class:: sphx-glr-horizontal


    *

      .. image:: /sphx_glr_plot_1.png
            :class: sphx-glr-multi-img

    *

      .. image:: /second.png
            :class: sphx-glr-multi-img
"""
    assert image_rst == image_list_rst

    # test issue #229
    local_img = [os.path.join(os.getcwd(), 'third.png')]
    image_rst = figure_rst(local_img, '.')

    single_image = SINGLE_IMAGE % "third.png"
    assert image_rst == single_image


def test_iterator():
    """Test ImagePathIterator."""
    ipi = ImagePathIterator('foo{0}')
    ipi._stop = 10
    with pytest.raises(RuntimeError, match='10 images'):
        for ii in ipi:
            pass
