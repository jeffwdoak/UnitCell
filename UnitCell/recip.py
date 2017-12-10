#!/usr/bin/env python

"""
Script to calculate and print to stdout the reciprocal-space lattice vectors of
a unitcell.

"""

import sys

from unitcell import UnitCell

with open(sys.argv[1], 'r') as cell_file:
    cell = UnitCell(cell_file)
recip, b = cell.recip_lat()
print recip
print
print b
