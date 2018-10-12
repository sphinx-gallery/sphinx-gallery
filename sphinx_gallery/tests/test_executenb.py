import codecs
import os
import re

from sphinx_gallery.gen_rst import MixedEncodingStringIO
import sphinx_gallery.gen_rst as sg
from sphinx_gallery.tests.test_gen_rst import CONTENT


def test_executenb(gallery_conf):
    gallery_conf.update(filename_pattern=re.escape(os.sep) + 'plot_0')
    gallery_conf.update(executor='notebook')

    code_output = ('\n Out:\n\n .. code-block:: none\n'
                   '\n'
                   '    Óscar output\n'
                   '    log:Óscar\n'
                   '    $\\langle n_\\uparrow n_\\downarrow \\rangle$\n\n'
                   )
    # create three files in tempdir (only one matches the pattern)
    fnames = ['plot_0.py', 'plot_1.py', 'plot_2.py']
    for fname in fnames:
        with codecs.open(os.path.join(gallery_conf['examples_dir'], fname),
                         mode='w', encoding='utf-8') as f:
            f.write('\n'.join(CONTENT))
        # generate rst file
        sg.generate_file_rst(fname, gallery_conf['gallery_dir'],
                             gallery_conf['examples_dir'], gallery_conf)
        # read rst file and check if it contains code output
        rst_fname = os.path.splitext(fname)[0] + '.rst'
        with codecs.open(os.path.join(gallery_conf['gallery_dir'], rst_fname),
                         mode='r', encoding='utf-8') as f:
            rst = f.read()
        if re.search(gallery_conf['filename_pattern'],
                     os.path.join(gallery_conf['gallery_dir'], rst_fname)):
            assert code_output in rst
        else:
            assert code_output not in rst
