# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:44:57 2015

@author: oscar
"""

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure


class glr_thumb(nodes.General, nodes.Element):
    """General docutils node to track the sphinx gallery thumbnails"""
    pass


def visit_glr_thumb(self, node):
    """Instructions to render the gallery thumbnails

    The containig div is first created. Later information is copied from
    the resolved link in the caption into the reference link on the image.
    This way the image becames clickable an links to the example.
    """
    snippet = node['tooltip']
    attrs = {"class": "sphx-glr-thumbContainer",
             "tooltip": snippet}

    self.body.append(self.starttag(node, "div", **attrs))

    # Puts the resolved reference of the caption into the image
    # If references could not be solved, empty link in the caption. But
    # important to bring attention which file is not resolved
    try:
        node[0][0]['refuri'] = node[0][1][0]['refuri']
    except KeyError:
        raise KeyError('Could not resolve reference {rawsource}'
                       ' in file {source}'.format(**node[0][1].__dict__))


def depart_glr_thumb(self, node):
    self.body.append('</div>\n')


class GlrThumb(Figure):
    """Local Directive to hold the sphinx gallery thumbnail

    The figure directive is nested in this directive allowing to allocate
    newer options"""

    option_spec = Figure.option_spec.copy()
    option_spec['tooltip'] = directives.unchanged_required

    def run(self):
        self.options['target'] = u'#'
        (figure_node, ) = Figure.run(self)
        if isinstance(figure_node, nodes.system_message):
            return [figure_node]

        thumbnail_node = glr_thumb('', figure_node)

        thumbnail_node['tooltip'] = self.options.pop('tooltip', None)

        return [thumbnail_node]


def setup(app):

    app.add_node(glr_thumb, html=(visit_glr_thumb, depart_glr_thumb))
    app.add_directive('glr_thumb', GlrThumb)
