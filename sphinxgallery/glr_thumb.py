# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:44:57 2015

@author: oscar
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.util import ws_re
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure


class glr_thumb(nodes.General, nodes.Element):
    pass


def visit_glr_thumb_node(self, node):
    snippet = node['tooltip']
    attrs = {"class": "sphx-glr-thumbContainer",
             "tooltip": snippet}
    self.body.append(self.starttag(node, "div", **attrs))

def depart_glr_thumb_node(self, node):
    self.body.append('</div>\n')


class GlrThumb(Figure):

    option_spec = Figure.option_spec.copy()
    option_spec['tooltip'] = directives.unchanged_required
    option_spec['reftarget'] = directives.unchanged_required

    def run(self):
        tar = self.options.pop('reftarget')
        target = ws_re.sub(' ', tar)
#        reference_node = addnodes.pending_xref(reftype='doc',
#                                               reftarget=target,
#                                               refexplicit='')
        (figure_node, ) = Figure.run(self)
        if isinstance(figure_node, nodes.system_message):
            return [figure_node]

#        reference_node += figure_node

#        return [reference_node]
        tno = glr_thumb('', figure_node)
        tno['tooltip'] = self.options.pop('tooltip', None)

        return [tno]


def setup(app):

    app.add_node(glr_thumb, html=(visit_glr_thumb_node, depart_glr_thumb_node))
    app.add_directive('glr_thumb', GlrThumb)
