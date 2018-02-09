# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function

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


def test_identify_names(unicode_sample):

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

    res = sg.identify_names(unicode_sample)
    assert expected == res


def test_identify_names2(tmpdir):
    code_str = b"""
'''
Title
-----

This is an example.
'''
# -*- coding: utf-8 -*-
# \xc3\x9f
from a.b import c
import d as e
print(c)
e.HelloWorld().f.g
"""
    expected = {'c': {'name': 'c', 'module': 'a.b', 'module_short': 'a.b'},
                'e.HelloWorld': {'name': 'HelloWorld', 'module': 'd', 'module_short': 'd'}}

    fname = tmpdir.join("indentify_names.py")
    fname.write(code_str, 'wb')

    res = sg.identify_names(fname.strpath)

    assert expected == res

    code_str = b"""
'''
Title
-----

This example uses :func:`h.i`.
'''
""" + code_str.split(b"'''")[-1]
    expected['h.i'] = {u'module': u'h', u'module_short': u'h', u'name': u'i'}

    fname = tmpdir.join("indentify_names.py")
    fname.write(code_str, 'wb')

    res = sg.identify_names(fname.strpath)

    assert expected == res
