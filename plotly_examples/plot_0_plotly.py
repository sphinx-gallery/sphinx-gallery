"""
========================================
Example with the plotly graphing library
========================================

Sphinx-Gallery supports examples made with the `plotly library`_. To use
plotly, add its scraper to the list of :ref:`image_scrapers` in the
``conf.py`` of the project::

    sphinx_gallery_conf = {
        ...
        "image_scrapers": ("matplotlib", "plotly"),
    }

The scraper embeds every figure displayed with ``fig.show()`` as interactive
HTML, and also every figure that is the last expression of a code block
(see :ref:`capture_repr`), as in the examples below. Each figure is
additionally exported as a static image so that it can serve as the example
thumbnail, which requires `kaleido
<https://plotly.com/python/static-image-export/>`_ and a Chromium-based web
browser; without them a warning is emitted and examples get a placeholder
thumbnail.

This tutorial gives a few examples of plotly figures, starting with its
high-level API `plotly express <https://plotly.com/python/plotly-express/>`_.

.. _plotly library: https://plotly.com/python/
"""

import numpy as np
import plotly.express as px

df = px.data.tips()
fig = px.bar(
    df,
    x="sex",
    y="total_bill",
    facet_col="day",
    color="smoker",
    barmode="group",
    template="presentation+plotly",
)
fig.update_layout(height=400)
fig

# %%
# In addition to the classical scatter or bar charts, plotly provides a large
# variety of traces, such as the sunburst hierarchical trace of the following
# example. plotly is an interactive library: click on one of the continents
# for a more detailed view of the drill-down.

df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(
    df,
    path=["continent", "country"],
    values="pop",
    color="lifeExp",
    hover_data=["iso_alpha"],
    color_continuous_scale="RdBu",
    color_continuous_midpoint=np.average(df["lifeExp"], weights=df["pop"]),
)
fig.update_layout(title_text="Life expectancy of countries and continents")
fig


# %%
# While plotly express is often the high-level entry point of the plotly
# library, complex figures mixing different types of traces can be made
# with the low-level ``graph_objects`` imperative API.

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, specs=[[{}, {"type": "domain"}]])
fig.add_trace(go.Bar(x=[2018, 2019, 2020], y=[3, 2, 5], showlegend=False), 1, 1)
fig.add_trace(go.Pie(labels=["A", "B", "C"], values=[1, 3, 6]), 1, 2)
fig.update_layout(height=400, template="presentation", yaxis_title_text="revenue")
fig
