"""
========================================
Example with the plotly graphing library
========================================

Sphinx-Gallery supports examples made with the
`plotly library <https://plotly.com/python/>`_. Sphinx-Gallery is able to
capture the ``_repr_html_`` of plotly figure objects (see :ref:`capture_repr`).
To display the figure, the last line in your code block should therefore be
the plotly figure object.

In order to use plotly, the ``conf.py`` of the project should include the
following lines to select the appropriate plotly renderer::

    import plotly.io as pio
    pio.renderers.default = 'sphinx_gallery'

**Optional**: the ``sphinx_gallery`` renderer of plotly will not generate png
thumbnails. For png thumbnails, you can use instead the ``sphinx_gallery_png``
renderer, and add ``plotly.io._sg_scraper.plotly_sg_scraper`` to the list of
:ref:`image_scrapers`. The scraper requires you to
`install the orca package <https://plotly.com/python/static-image-export/>`_.

This tutorial gives a few examples of plotly figures, starting with its
high-level API `plotly express <https://plotly.com/python/plotly-express/>`_.
"""
import plotly.express as px
import numpy as np

df = px.data.tips()
fig = px.bar(df, x='sex', y='total_bill', facet_col='day', color='smoker', barmode='group',
             template='presentation+plotly'
             )
fig.update_layout(height=400)
fig

#%%
# In addition to the classical scatter or bar charts, plotly provides a large
# variety of traces, such as the sunburst hierarchical trace of the following
# example. plotly is an interactive library: click on one of the continents
# for a more detailed view of the drill-down.

df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(title_text='Life expectancy of countries and continents')
fig


#%%
# While plotly express is often the high-level entry point of the plotly
# library, complex figures mixing different types of traces can be made
# with the low-level ``graph_objects`` imperative API.

from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=1, cols=2, specs=[[{}, {'type':'domain'}]])
fig.add_trace(go.Bar(x=[2018, 2019, 2020], y=[3, 2, 5], showlegend=False), 1, 1)
fig.add_trace(go.Pie(labels=['A', 'B', 'C'], values=[1, 3, 6]), 1, 2)
fig.update_layout(height=400, template='presentation', yaxis_title_text='revenue')
fig

# sphinx_gallery_thumbnail_path = '_static/plotly_logo.png'
