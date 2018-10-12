"""
Pandas DataFrame
================

This example doesn't do much, it just shows a dataframe
"""
import pandas as pd
import numpy as np
x = np.arange(100)
y = x**2
df = pd.DataFrame(data=dict(x=x, y=y))
df