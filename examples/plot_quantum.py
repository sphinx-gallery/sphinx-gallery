# -*- coding: utf-8 -*-
r"""
======================
Some Quantum Mechanics
======================

We start with a two spin system :math:`\uparrow` and :math:`\downarrow`

"""
# Author: Óscar Nájera

from __future__ import division, absolute_import, print_function


def hamiltonian(M, mu):
    r"""Generate a single orbital isolated atom Hamiltonian in particle-hole
    symmetry. Include chemical potential for grand Canonical calculations

    .. math::
        \mathcal{H} - \mu N = M(n_\uparrow - n_\downarrow)
        - \mu(n_\uparrow + n_\downarrow)
    """
    pass

###############################################################################
# Double occupation
# -----------------
#
# To find out the double occupation one uses the relation
# (Works in Sphinx-Gallery)

import matplotlib.pylab as plt
import numpy as np
x = np.linspace(0, 1, 20)
plt.plot(x, (1 - x**2) / 4)
plt.ylabel('$\\langle n_\\uparrow n_\\downarrow \\rangle$')
plt.show()

###############################################################################
#
# .. math:: \langle n_\uparrow n_\downarrow \rangle = \frac{2\langle V \rangle}{U}+\frac{1}{4}

print('pass')

###############################################################################
# (Does not work in Sphinx-Gallery)
# ---------------------------------

plt.plot(x, (1 - x) / 4)
plt.ylabel(r'$\langle n_\uparrow n_\downarrow \rangle$')
plt.xlabel('U')
plt.show()
