Sphinx-Gallery
==============
[![Build Status](https://travis-ci.org/sphinx-gallery/sphinx-gallery.svg?branch=master)](https://travis-ci.org/sphinx-gallery/sphinx-gallery)
[![Documentation Status](https://readthedocs.org/projects/sphinx-gallery/badge/?version=latest)](https://readthedocs.org/projects/sphinx-gallery/?badge=latest)

Sphinx extension for automatic generation of an example gallery.

Getting the package
-------------------

You can do a direct install via pip by using

```
$ pip install sphinxgallery
```

### Install as developer


You can get the latest development source from our Github repository.
You need `setuptools` installed in your system to install. A future migration
to the standard distutils is planned.

You will also need have installed:
* Sphinx
* matplotlib
* pillow
* scikit-learn

But if you don't the `setuptools` will try to install them for you


```
$ git clone https://github.com/sphinx-gallery/sphinx-gallery
$ cd sphinx-gallery
$ python setup.py develop
```

Setting up your project
-----------------------

After installing you need to include in your Sphinx `conf.py` file:


```python
extensions = [
    ...
    'sphinxgallery.gen_rst',
    ]

import sphinxgallery
html_static_path = ['_static', sphinxgallery._path_static()]

```
you need to have a folder called `examples` in your main repository directory.
This folder needs

* A `README.txt` file with rst syntax to present your gallery
* `plot_examples.py` files. Python scripts that have to be executed
  and output a plot that will be presented in your gallery
* `examples.py` files. Python scripts that will not be executed but will be presented
  in the gallery

Your python scripts in the examples folder need to have a main comment. Written
in rst sintax to be used in the generated file in the example gallery.

If these instructions are not clear enough, this package uses itself, to generated
its own example gallery. So check the directory structure and the contents of the
files.

That is all, our module shall take care of the rest


