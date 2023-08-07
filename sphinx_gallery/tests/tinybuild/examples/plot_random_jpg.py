"""
Capture JPG test
================
Test that it is possible to capture a JPG from a class with a ``_repr_jpeg__``
method.
"""


# sphinx_gallery_capture_repr = ('_repr_jpeg_',)
import io
import numpy
from PIL import Image


class RandomImage:
    def __init__(self):
        imarray = numpy.random.rand(160, 160, 3) * 255
        self._image = Image.fromarray(imarray.astype('uint8')).convert('RGB')

    def _repr_jpeg_(self):
        b = io.BytesIO()
        self._image.save(b, "JPEG")
        return b.getvalue()


RandomImage()
