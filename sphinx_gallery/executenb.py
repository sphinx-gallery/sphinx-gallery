import json
import os

import nbformat
from jupyter_client.kernelspec import get_kernel_spec
from nbconvert.preprocessors.execute import executenb
from nbconvert.exporters.exporter import Exporter

from .gen_rst import indent, CODE_OUTPUT

# the first cell of the notebook will output information on memory usage and the current time
CODE_PRE = r"""
%%matplotlib inline
import sys
src_file = %r
sys.argv = [src_file]
memory = -1
try:
    from memory_profiler import memory_usage
    memory_usage, _ = memory_usage(lambda: None, max_usage=True, retval=True, multiprocess=True)
except:
    pass
import time
time = time.time()
display({'application/json': {'memory_usage': memory, 'time': time}}, raw=True)
"""

# after each cell, we again output the memory and current time for statistics

CODE_POST_CELL = """
memory = -1
try:
    from memory_profiler import memory_usage
    memory_usage, _ = memory_usage(lambda: None, max_usage=True, retval=True, multiprocess=True)
except:
    pass
import time
time = time.time()
display({'application/json': {'memory_usage': memory, 'time': time}}, raw=True)
"""

CODE_CELL = """
%s
"""

# in the last cell, we collect a possible widget state, and again the time
CODE_POST = """
state = None
try:
    import ipywidgets as widgets
    state = widgets.Widget.get_manager_state()
except:
    pass
display({'application/json': state}, raw=True)

import time
time = time.time()
display({'application/json': {'time': time}}, raw=True)
"""

_mime_renderer = {}
def mime_renderer_jupyter_widgets(json_data):
    import ipywidgets.embed
    html_snippet = ipywidgets.embed.widget_view_template.format(view_spec=json.dumps(json_data))
    return mime_renderer_text_html(html_snippet)

def mime_renderer_image_png(json_data):
    html_snippet = '<img src="data:image/png;base64,%s"/>' % json_data
    return mime_renderer_text_html(html_snippet)

def mime_renderer_text_plain(json_data):
    return 'plain text'


def mime_renderer_text_html(json_data):
    html = """
 .. raw:: html

 {0}""".format(indent(json_data, u' ' * 4))
    return html

from base64 import b64decode


# ordered by priority, maybe we could use nbconvert for this
_mime_renderers = [
    ('application/vnd.jupyter.widget-view+json', mime_renderer_jupyter_widgets),
    ('text/html',  mime_renderer_text_html),
    ('image/png',  mime_renderer_image_png),
    ('text/plain', mime_renderer_text_plain)
]

def execute_script_notebook(script_blocks, script_vars, gallery_conf):
    kernel_name = gallery_conf.get('jupyter_kernel', 'python3')
    kernel_spec = get_kernel_spec(kernel_name)

    nb = nbformat.v4.new_notebook( metadata={'kernelspec': {
                'display_name': kernel_spec.display_name,
                'language': kernel_spec.language,
                'name': kernel_name,
            }})
    
    cell_pre = nbformat.v4.new_code_cell(CODE_PRE % script_vars['src_file'])
    nb['cells'].append(cell_pre)

    for block in script_blocks:
        blabel, bcontent, lineno = block
        if not script_vars['execute_script'] or blabel == 'text':
            cell = nbformat.v4.new_code_cell('# placeholder for text block')
        else:
            cell = nbformat.v4.new_code_cell(CODE_CELL % bcontent)
        nb['cells'].append(cell)
        cell = nbformat.v4.new_code_cell(CODE_POST_CELL)
        nb['cells'].append(cell)
    
    cell_post = nbformat.v4.new_code_cell(CODE_POST)
    nb['cells'].append(cell_post)

    # this will execute the notebook and populate the cells
    from nbconvert.preprocessors import ExecutePreprocessor, CSSHTMLHeaderPreprocessor
    from nbconvert.preprocessors.snapshot import SnapshotPreProcessor
    nbconvert_snapshot_config = gallery_conf.get('nbconvert', {}).get('snapshot', {})

    src_file = script_vars['src_file']
    cwd = os.getcwd()
    os.chdir(os.path.dirname(src_file))
    try:
        preprocessors = [ExecutePreprocessor(enabled=True, allow_errors=False), CSSHTMLHeaderPreprocessor(enabled=True), SnapshotPreProcessor(enabled=True, **nbconvert_snapshot_config)]
        exporter = Exporter(preprocessors=preprocessors, default_preprocessors=[])
        nb, resources = exporter.from_notebook_node(nb, {})
    finally:
        os.chdir(cwd)

    cell_pre  = nb.cells[0]
    cell_post = nb.cells[-1]


    memory_start = cell_pre.outputs[0]['data']['application/json']['memory_usage']
    time_start =  cell_pre.outputs[0]['data']['application/json']['time']

    output_blocks = []
    memory_usage = []

    # we have a pre cell, for each code block 2 cells, and a post cell
    for code_cell, info_cell in zip(nb.cells[1:-1:2], nb.cells[2:-1:2]):
        my_stdout_parts = []
        extra_output_parts = []
        for output in code_cell.outputs:
            if output['output_type'] == 'stream':
                if output['name'] == 'stdout':
                    my_stdout_parts.append(output['text'])
                elif output['name'] == 'stderr':
                    print('warning, stderr detected', output['text'])
            if 'data' in output:# == 'display_data':
                renderered = False
                for mime_type, renderer in _mime_renderers:
                    if mime_type in output['data']:
                        extra_output_parts.append(renderer(output['data'][mime_type]))
                        renderered = True
                        break
                if 'image/png' in output['data']:
                    image_path_iterator = script_vars['image_path_iterator']
                    path = next(image_path_iterator)
                    print('save to', path)
                    with open(path, 'wb') as f:
                        image_data = b64decode(output['data'][mime_type])
                        f.write(image_data)
                else:
                    pass  # here we could support other images, and make a screenshot of a widget or HTML/pdf even

                if not renderered:
                    raise ValueError('cell not rendered')

        my_stdout = ''.join(my_stdout_parts).strip().expandtabs()
        if my_stdout:
            stdout = CODE_OUTPUT.format(indent(my_stdout, u' ' * 4))
        else:
            stdout = ''

        images_rst = ''
        code_output = u"\n{0}\n\n{1}\n\n".format(images_rst, stdout)
        code_output += '\n\n'.join(extra_output_parts) 
        output_blocks.append(code_output)

        assert len(info_cell.outputs) == 1
        memory_usage.append(info_cell.outputs[0]['data']['application/json']['memory_usage'])

    if output_blocks:
        widget_state = cell_post.outputs[0]['data']['application/json']
        if widget_state:
            import ipywidgets.embed
            widget_state_html_snippet = ipywidgets.embed.snippet_template.format(load='', widget_views='', json_data=json.dumps(widget_state))
            output_blocks[-1] = output_blocks[-1] + '\n\n' + mime_renderer_text_html(widget_state_html_snippet)

    time_end =  cell_post.outputs[1]['data']['application/json']['time']
    script_vars['memory_delta'] = (max(memory_usage) - memory_start)
    return output_blocks, time_end - time_start
