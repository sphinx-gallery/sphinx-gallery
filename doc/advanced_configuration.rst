======================
Advanced Configuration
======================

Changing default directories
============================

Within your Sphinx ``conf.py`` file you need to add a configuration dictionary:

.. code-block:: python

    DEFAULT_CONF = {
        'root_dir'          : '../examples',              # path to your examples scripts
        'examples_gallery'  : 'auto_examples'}            # path where to save gallery generated examples


Directory paths are relative to your ``conf.py`` location.

Linking to external documentations
==================================



Establishing local calls to examples
====================================


.. include:: modules/generated/numpy.linspace.examples
.. raw:: html

    <div style='clear:both'></div>

.. include:: modules/generated/numpy.exp.examples
.. raw:: html

    <div style='clear:both'></div>
