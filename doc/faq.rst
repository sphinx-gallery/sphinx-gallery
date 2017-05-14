Frequently Asked Questions
==========================

.. contents:: **Contents**
    :local:
    :depth: 1


Why is `__file__` not defined? What can I use?
----------------------------------------------

The global `__file__` variable defined by Python when running scripts
is not defined on Jupyter notebooks. Since Sphinx-Gallery supports
notebook styled examples and also exports to Jupyter notebooks we
agreed on keeping this variable out of scope when executing the
example scripts.

Instead of `__file__` use :func:`os.getcwd` to get the directory where
the file is located. Sphinx-Gallery executes the examples scripts in
their source directory.


.. seealso::
    `Github PR #166 <https://github.com/sphinx-gallery/sphinx-gallery/pull/166>`_
    `Github PR #212 <https://github.com/sphinx-gallery/sphinx-gallery/pull/212>`_
