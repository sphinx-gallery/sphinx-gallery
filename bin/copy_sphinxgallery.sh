#!/bin/sh
# Script to do a local install of sphinx-gallery
rm -rf tmp sphinxgallery

easy_install -Zeab tmp sphinx-gallery

cp -vru tmp/sphinx-gallery/sphinxgallery/ .

git add sphinxgallery
