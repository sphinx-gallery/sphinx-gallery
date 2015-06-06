# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Testing the rst files generator
"""
from __future__ import division, absolute_import, print_function
from sphinxgallery import Path
import tempfile


def test_path():
    tmp_dir = Path(tempfile.mkdtemp())
    assert tmp_dir.exists
    assert tmp_dir.isdir

    tmp_file = tmp_dir.pjoin('test.txt')
    assert tmp_file.psplit() == [tmp_dir, 'test.txt']
    assert tmp_dir.pjoin('a', 'o').psplit() == [tmp_dir.pjoin('a'), 'o']

    with open(tmp_file, 'w') as test_file:
        test_file.write('testing')
    in_dir = tmp_dir.pjoin('in_dir')
    in_dir.makedirs()
    assert set(tmp_dir.listdir()) == set(['test.txt', 'in_dir'])

    file_name = Path('file{:03}.png')
    assert file_name.format(15) == 'file015.png'
