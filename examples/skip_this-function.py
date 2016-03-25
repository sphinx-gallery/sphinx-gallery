"""

=======================
This example is not run
=======================

The code in this example should not be run because we will exclude
it from processing using a regular expression to ignore any file
that begins with 'skip_'. We do this by setting
``filename_pattern = '^((?!skip_).)*$'``

"""

print("Output from this print should not appear!")

##################################################################
# More text.
#

print("This output shouldn't appear either!!!")
