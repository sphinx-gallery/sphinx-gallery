# -*- coding: utf-8 -*-
r"""
Some Quantum Mechanics, filling an atomic orbital
=================================================

Considering an atomic single orbital and how to fill it by use of the
chemical potential. This system has a four element basis, :math:`B =
\{ \lvert \emptyset \rangle, \lvert \uparrow \rangle, \lvert
\downarrow \rangle, \lvert \uparrow\downarrow \rangle \}`, that is the
empty orbital, one spin up electron, one spin down electron and the
filled orbital.

The environment of the orbital is set up by an energy cost for
occupying the orbital, that is :math:`\epsilon` and when both
electrons meet a contact interaction corresponding to the Coulomb
repulsion :math:`U`. Finally the chemical potential :math:`\mu` is
what allows in the Grand canonical picture, to fill up our atomic
orbital from a reservoir of electrons.

 The the simple Hamiltonian to model this system is given by:

.. math::
   \mathcal{H} =
        \sum_{\sigma=\uparrow,\downarrow} \epsilon c^\dagger_\sigma c_\sigma
       + Un_\uparrow n_\downarrow - \mu \hat{N}

Here :math:`c^\dagger,c` creation and annihilation operators,
:math:`n=c^\dagger c`, and
:math:`\hat{N}=n_\uparrow+n_\downarrow`. This Hamiltonian is diagonal
in the basis of particle number we have chosen earlier, as the basis
elements are also eigenvectors.

.. math::
   \mathcal{H} \lvert \emptyset \rangle &= 0 \\
   \mathcal{H} \lvert \uparrow  \rangle &= (\epsilon - \mu) | \uparrow  \rangle \\
   \mathcal{H} \lvert \downarrow  \rangle &= (\epsilon - \mu) | \downarrow  \rangle \\
   \mathcal{H} \lvert \uparrow\downarrow \rangle &= (2\epsilon - 2\mu +U) \lvert \uparrow\downarrow \rangle

It is easy to see, that the system will prefer to be empty if
:math:`\mu \in [0,\epsilon)`, be single occupied if :math:`\mu \in (\epsilon, \epsilon +U)`
and doubly occupied if :math:`\mu > \epsilon +U`.

For a more rigorous treatment, the partition function has to be
calculated and then the expected particle number can be
found. Introducing a new variable :math:`\xi = \epsilon - \mu`, and
:math:`\beta` corresponding to the inverse temperature of the system.

.. math::
   \mathcal{Z} &= Tr(e^{-\beta \mathcal{H}}) = 1 + 2e^{-\beta\xi} + e^{-\beta(2\xi + U)} \\
   \langle \hat{N} \rangle &= \frac{1}{\beta} \frac{\partial}{\partial \mu} \ln \mathcal{Z}
"""

# Code source: Óscar Nájera
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
mu = np.linspace(0, 3, 800)
for b in [10, 20, 30]:
    n = 2 * (np.exp(b * (mu - 1)) + np.exp(b * (2 * mu - 3))) / \
        (1 + np.exp(b * (mu - 1)) * (2 + np.exp(b * (mu - 2))))
    plt.plot(mu, n, label=r"$\beta={0}$".format(b))
plt.xlabel(r'$\mu$ ($\epsilon=1$, $U=1$)')
plt.ylabel(r'$\langle N \rangle=\langle n_\uparrow \rangle+\langle n_\downarrow\rangle$')
plt.legend(loc=0)
plt.show()
