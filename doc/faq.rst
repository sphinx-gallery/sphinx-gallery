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

Why am I getting text output for Matplotlib functions?
------------------------------------------------------

The output capturing behavior of Sphinx-Gallery changed with Sphinx-Gallery
v0.5.0. Previous to v0.5.0, only data directed to standard output (e.g., only
Matplotlib figures) was captured. In, v0.5.0, the configuration
``'capture_repr'`` (:ref:`capture_repr`) was added. This configuration allows a
'representation' of the last statement of each code block, if it is an
expression, to be captured. The default setting of this new configuration,
``'capture_repr': ('_repr_html_', '__repr__')``, first attempts to capture the
``'_repr_html_'`` and if this does not exist, the ``'__repr__'``. This means
that if the last statement was a Matplotlib function, which usually returns a
value, the representation of that value will be captured as well.

To prevent Matplotlib function calls from outputting text as well as the figure,
you can assign the last plotting function to a temporary variable (e.g.
``_ = matplotlib.pyploy.plot()``) or add ``matplotlib.pyplot.show()`` to the
end of your code block (see :ref:`capture_repr`).
Alternatively, you can set ``capture_repr`` to be an empty tuple
(``'capture_repr': ()``), which will imitate the behavior of Sphinx-Gallery
prior to v0.5.0. This will also prevent you from getting any other unwanted
output that did not occur prior to v0.5.0.

Why has my thumbnail appearance changed?
----------------------------------------

The DOM structure of thumbnails was refactored in order to make them responsive
and aligned on a css grid. These changes might make your existing custom css
obsolete. You can read our
`custom css migration guide for thumbnails <https://github.com/sphinx-gallery/sphinx-gallery/pull/906#issuecomment-1019542067>`_
for pointers on how to update your css.


.. seealso::
    `Github PR #906 <https://github.com/sphinx-gallery/sphinx-gallery/pull/906>`_
