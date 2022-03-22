# -*- coding: utf-8 -*-
"""
Showing expected error outputs
==============================

This example demonstrates how to include expected exceptions in your gallery
examples.
"""
#%%
# The following code raises an error:

# sphinx_gallery_expected_error
# TODO 1 + "hello"

# %%
# But this runs without error:

1 * "hello"

#%%
# You may wish to restrict the type of the expected exception caught
# (This may look familiar to ``pytest`` users)

# sphinx_gallery_expected_error : TypeError
# TODO 1 + "hello"
