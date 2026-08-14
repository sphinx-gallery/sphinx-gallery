"""
No parallel
-----------

This example opts out of parallel execution.
"""

import multiprocessing

# sphinx_gallery_parallel = False

assert multiprocessing.parent_process() is None, "did not run in the main process"
print("ran serially")
