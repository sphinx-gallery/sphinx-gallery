# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
import os
import tempfile
import sphinx_gallery.backreferences as sg


def test_thumbnail_div():
    """Test if the thumbnail div generates the correct string"""

    html_div = sg._thumbnail_div('fake_dir', 'test_file.py', '<"test">')

    reference = r"""
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="&lt;&quot;test&quot;&gt;">

.. only:: html

    .. figure:: /fake_dir/images/thumb/sphx_glr_test_file_thumb.png

        :ref:`sphx_glr_fake_dir_test_file.py`

.. raw:: html

    </div>
"""

    assert html_div == reference


def test_backref_thumbnail_div():
    """Test if the thumbnail div generates the correct string"""

    html_div = sg._thumbnail_div('fake_dir', 'test_file.py', 'test formating',
                                 is_backref=True)

    reference = """
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="test formating">

.. only:: html

    .. figure:: /fake_dir/images/thumb/sphx_glr_test_file_thumb.png

        :ref:`sphx_glr_fake_dir_test_file.py`

.. raw:: html

    </div>

.. only:: not html

    * :ref:`sphx_glr_fake_dir_test_file.py`
"""

    assert html_div == reference


def test_identify_names():

    expected = {
        'os.path.join':
            {'name': 'join', 'module': 'os.path', 'module_short': 'os.path'},
        'br.identify_names':
            {'name': 'identify_names',
             'module': 'sphinx_gallery.back_references',
             'module_short': 'sphinx_gallery.back_references'},
        'identify_names':
            {'name': 'identify_names',
             'module': 'sphinx_gallery.back_references',
             'module_short': 'sphinx_gallery.back_references'}
    }

    res = sg.identify_names('sphinx_gallery/tests/unicode.sample')
    assert expected == res


def test_identify_names2():
    code_str = b"""
# -*- coding: utf-8 -*-
# \xc3\x9f
from a.b import c
import d as e
print(c)
e.HelloWorld().f.g
"""
    expected = {'c': {'name': 'c', 'module': 'a.b', 'module_short': 'a.b'},
                'e.HelloWorld': {'name': 'HelloWorld', 'module': 'd', 'module_short': 'd'}}

    import locale
    print(locale.getlocale())

    with tempfile.NamedTemporaryFile('wb', delete=False) as f:
        f.write(code_str)
    try:
        res = sg.identify_names(f.name)
    finally:
        os.remove(f.name)

    assert expected == res
