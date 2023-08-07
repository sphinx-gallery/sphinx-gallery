"""
Capture PNG test
================
Test that it is possible to capture a PNG of a Pillow Image
(which has a ``_repr_png_`` method).
"""


# sphinx_gallery_capture_repr = ('_repr_png_',)
import numpy
from PIL import Image


imarray = numpy.random.rand(160, 160, 3) * 255
Image.fromarray(imarray.astype('uint8')).convert('RGB')
