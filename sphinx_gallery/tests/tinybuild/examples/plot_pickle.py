"""
Pickling
--------

This example pickles a function.
"""
import pickle

assert __name__ == '__main__'
assert '__file__' not in globals()


def function():
    pass


pickle.loads(pickle.dumps(function))
