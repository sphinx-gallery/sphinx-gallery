"""
Custom Sphinx directives
========================
"""

import os

from docutils import statemachine
from docutils.parsers.rst import Directive, directives


class MiniGallery(Directive):
    """
    Custom directive to insert a mini-gallery

    The required argument is one or more fully qualified names of objects,
    separated by spaces.  The mini-gallery will be the subset of gallery
    examples that make use of that object (from that specific namespace).

    Options:

    * `add-heading` adds a heading to the mini-gallery.  If an argument is
      provided, it uses that text for the heading.  Otherwise, it uses
      default text.
    * `heading-level` specifies the heading level of the heading as a single
      character.  If omitted, the default heading level is `'^'`.
    """
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'add-heading': directives.unchanged,
                   'heading-level': directives.single_char_or_unicode}

    def run(self):
        # Respect the same disabling options as the `raw` directive
        if (not self.state.document.settings.raw_enabled
                or not self.state.document.settings.file_insertion_enabled):
            raise self.warning('"%s" directive disabled.' % self.name)

        # Retrieve the backreferences directory
        config = self.state.document.settings.env.config
        backreferences_dir = config.sphinx_gallery_conf['backreferences_dir']

        # Parse the argument into the individual objects
        obj_list = self.arguments[0].split()

        lines = []

        # Add a heading if requested
        if 'add-heading' in self.options:
            heading = self.options['add-heading']
            if heading == "":
                if len(obj_list) == 1:
                    heading = 'Examples using ``{}``'.format(obj_list[0])
                else:
                    heading = 'Examples using one of multiple objects'
            lines.append(heading)
            heading_level = self.options.get('heading-level', '^')
            lines.append(heading_level * len(heading))

        # Insert the backreferences file(s) using the `include` directive
        for obj in obj_list:
            path = os.path.join('/',  # Sphinx treats this as the source dir
                                backreferences_dir,
                                '{}.examples'.format(obj))

            # Always remove the heading (first 5 lines) from the file
            lines.append('.. include:: {}\n    :start-line: 5'.format(path))

        # Insert the end for the gallery using the `raw` directive
        lines.append('.. raw:: html\n\n    <div class="sphx-glr-clear"></div>')

        # Parse the assembly of `include` and `raw` directives
        text = '\n'.join(lines)
        include_lines = statemachine.string2lines(text,
                                                  convert_whitespace=True)
        self.state_machine.insert_input(include_lines, path)

        return []
