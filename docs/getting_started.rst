===============
Getting Started
===============

Getting the package
===================
The package can be directly obtained via pip by using::

  $ pip install sphinxgallery


Setting up your project
=======================
After installing you need to include in your Sphinx **conf.py** file:

.. code-block:: python

    extensions  [
        ...
        'sphinxgallery.gen_rst',
        ]

    import sphinxgallery
    html_static_path = ['_static', sphinxgallery._path_static()]


you need to have a folder called **examples** in your main repository directory.
This folder needs

* A **README.txt** file with rst syntax to present your gallery
* **plot_examples.py** files. Python scripts that have to be executed
  and output a plot that will be presented in your gallery
* **examples.py** files. Python scripts that will not be executed but will be presented
  in the gallery

Your python scripts in the examples folder need to have a main comment. Written
in rst syntax to be used in the generated file in the example gallery.

You can have subfolders in your **examples** directory, those will be recursively
scaned by the gallery extension and presented in the gallery. Subfolder have to
respect the same structure of the main **examples** folder.

If these instructions are not clear enough, this package uses itself, to generated
its own example gallery. So check the directory structure and the contents of the
files.

Once you build the documentation, our extension will generate a **auto_examples**
directory and populate it with rst files containing the gallery and each example.
Then Sphinx will give this files its regular processing and you can enjoy your
generated gallery unde the same path.
