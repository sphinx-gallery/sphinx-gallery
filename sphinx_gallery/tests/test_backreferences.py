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


def test_identify_names():
    code_str = """
# ß
import os
os

os.path.join

import sphinx_gallery.back_references as br
br.identify_names

from sphinx_gallery.back_references import identify_names
identify_names
"""
    res = sg.identify_names(code_str)
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

    assert expected == res


# sg.scan_used_functions('sphinx_gallery/tests/unicode.sample', {'doc_module': 'numpy'})

# names = sg.identify_names('import ß\nß.help# ós\na=3\nimport os\nos.path')
# print(names)
# print(type(names))
# names = sg.identify_names(u'import a\na.help# ós\na=3\nimport os\nos.path')
# print(names)
# print(type(names))
#
# print(sg.scan_used_functions(
#'../../examples/plot_choose_thumbnail.py', {'doc_module': u'numpy'}))
# print('\nline\n')
# import codecs
# names = sg.identify_names(
# codecs.open('../../examples/plot_choose_thumbnail.py', 'r', 'utf-8').read())
#
# print(names)
# print(type(names))
