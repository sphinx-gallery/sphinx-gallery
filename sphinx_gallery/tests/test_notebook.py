# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
r"""
Testing the Jupyter notebook parser
"""

from __future__ import division, absolute_import, print_function
from collections import defaultdict
from itertools import count
import json
import tempfile
import os
import pytest
import re
import textwrap

import sphinx_gallery.gen_rst as sg
from sphinx_gallery.notebook import (rst2md, jupyter_notebook, save_notebook,
                                     python_to_jupyter_cli)


def test_latex_conversion():
    """Latex parsing from rst into Jupyter Markdown"""
    double_inline_rst = r":math:`T<0` and :math:`U>0`"
    double_inline_jmd = r"$T<0$ and $U>0$"
    assert double_inline_jmd == rst2md(double_inline_rst, {})

    align_eq = r"""
.. math::
   \mathcal{H} &= 0 \\
   \mathcal{G} &= D"""

    align_eq_jmd = r"""
\begin{align}\mathcal{H} &= 0 \\
   \mathcal{G} &= D\end{align}"""
    assert align_eq_jmd == rst2md(align_eq, {})


def test_convert():
    """Test ReST conversion"""
    rst = """hello

.. contents::
    :local:

This is :math:`some` math :math:`stuff`.

.. note::
    Interpolation is a linear operation that can be performed also on
    Raw and Epochs objects.

.. warning::
    Go away

For more details on interpolation see the page :ref:`channel_interpolation`.
.. _foo: bar

.. image:: foobar
  :alt: me
  :whatever: you
"""

    markdown = """hello

This is $some$ math $stuff$.

<div class="alert alert-info"><h4>Note</h4><p>Interpolation is a linear operation that can be performed also on
    Raw and Epochs objects.</p></div>

<div class="alert alert-danger"><h4>Warning</h4><p>Go away</p></div>

For more details on interpolation see the page `channel_interpolation`.

![me](foobar)
"""  # noqa
    assert rst2md(rst, {}) == markdown


def test_headings():
    rst = textwrap.dedent("""\
    =========
    Heading 1
    =========

    Heading 2
    =========

    =============
     Heading 1-2
    =============

    Heading 3
    ---------

    =============
    Not a Heading
    -------------
    Mismatch top and bottom

    Not another heading
    -=-=-=-=-=-=-=-=-=-
    Multiple characters

    -------
     Bad heading but okay
    -------------
    Over and under mismatch, not rendered and warning raised by Sphinx

    Another bad heading, but passable
    ^^^^^^^^^^^^^^^^^^^^^
    Too short, warning raised but is rendered by Sphinx

    A
    *

    BC
    **

    Some text
    And then a heading
    ------------------
    Not valid with no blank line above

    =======================
           Centered
    =======================

    ------------------------

    ------------------------
    Blank heading above.

                
    ====================
      White space above
    ====================

    """) # noqa

    heading_level_counter = count(start=1)
    heading_levels = defaultdict(lambda: next(heading_level_counter))
    text = rst2md(rst, heading_levels)

    assert text.startswith("# Heading 1\n")
    assert "\n## Heading 2\n" in text
    assert "\n# Heading 1-2\n" in text
    assert "\n### Heading 3\n" in text
    assert "# Not a Heading" not in text
    assert "# Not another Heading" not in text
    assert "\n#### Bad heading but okay\n" in text
    assert "\n##### Another bad heading, but passable\n" in text
    assert "\n###### A\n" in text
    assert "\n###### BC\n" in text
    assert "# And then a heading\n" not in text
    assert "\n# Centered\n" in text
    assert "#\nBlank heading above." not in text
    assert "# White space above\n" in text


def test_jupyter_notebook(gallery_conf):
    """Test that written ipython notebook file corresponds to python object."""
    file_conf, blocks = sg.split_code_and_text_blocks(
        'tutorials/plot_parse.py')
    example_nb = jupyter_notebook(blocks, gallery_conf)

    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        save_notebook(example_nb, f.name)
    try:
        with open(f.name, "r") as fname:
            assert json.load(fname) == example_nb
    finally:
        os.remove(f.name)
    assert example_nb.get('cells')[0]['source'][0] == "%matplotlib inline"

    # Test custom first cell text
    test_text = '# testing\n%matplotlib notebook'
    gallery_conf['first_notebook_cell'] = test_text
    example_nb = jupyter_notebook(blocks, gallery_conf)
    assert example_nb.get('cells')[0]['source'][0] == test_text

    # Test empty first cell text
    test_text = None
    gallery_conf['first_notebook_cell'] = test_text
    example_nb = jupyter_notebook(blocks, gallery_conf)
    cell_src = example_nb.get('cells')[0]['source'][0]
    assert re.match('^[\n]?# Alternating text and code', cell_src)

    # Test custom last cell text
    test_text = '# testing last cell'
    gallery_conf['last_notebook_cell'] = test_text
    example_nb = jupyter_notebook(blocks, gallery_conf)
    assert example_nb.get('cells')[-1]['source'][0] == test_text

    # Test empty first cell text
    test_text = None
    gallery_conf['last_notebook_cell'] = test_text
    example_nb = jupyter_notebook(blocks, gallery_conf)
    cell_src = example_nb.get('cells')[-1]['source'][0]
    assert re.match("^Last text block.\n\nThat[\\\\]?'s all folks !", cell_src)


###############################################################################
# Notebook shell utility


def test_with_empty_args():
    """ User passes no args, should fail with SystemExit """
    with pytest.raises(SystemExit):
        python_to_jupyter_cli([])


def test_missing_file():
    """ User passes non existing file, should fail with FileNotFoundError """
    with pytest.raises(FileNotFoundError) as excinfo:
        python_to_jupyter_cli(['nofile.py'])
    excinfo.match(r'No such file or directory.+nofile\.py')


def test_file_is_generated():
    """User passes good python file. Check notebook file is created"""

    python_to_jupyter_cli(['examples/plot_0_sin.py'])
    assert os.path.isfile('examples/plot_0_sin.ipynb')
    os.remove('examples/plot_0_sin.ipynb')
