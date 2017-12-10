#!/usr/bin/env python

"""
Calculate the spacegroup of a unitcell.

"""

import sys

from unitcell import UnitCell

with open(sys.argv[1], 'r') as poscar:
    unit_cell = UnitCell(poscar)
outfile = unit_cell.spacegroup()
print outfile
sys.exit()
