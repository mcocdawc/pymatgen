# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from pymatgen.core.spectrum import Spectrum
import numpy as np

"""
This module defines classes to represent all xas
"""

__author__ = "Chen Zheng"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "2.0"
__maintainer__ = "Chen Zheng"
__email__ = "chz022@ucsd.edu"
__date__ = "Aug 9, 2017"


class XANES(Spectrum):
    """
    Basic XANES object.

    Args:
        x: A sequence of x-ray energies in eV
        y: A sequence of mu(E)

    .. attribute: x
        The sequence of energies
    .. attribute: y
        The sequence of mu(E)
    .. attribute: absorption_specie
        The absorption_species of the spectrum
    .. attribute: edge
        The edge of XANES spectrum
    """
    XLABEL = 'Energy (eV)'
    YLABEL = 'Intensity (mu)'

    def __init__(self, x, y, structure, absorption_specie, edge):
        super(XANES, self).__init__(x, y, structure, absorption_specie, edge)
        self.structure = structure
        self.absorption_specie = absorption_specie
        self.edge = edge

    def find_e0(self):
        """
        Use the maximum gradient to find e0
        """
        self.e0 = self.x[np.argmax(np.gradient(self.y) / np.gradient(self.x))]

