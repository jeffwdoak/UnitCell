#!/usr/bin/env python

"""
Calculate center of mass of atomic positions (and velocities, if present) for a
unitcell.

"""

import sys

from unitcell import UnitCell

cell = UnitCell(open(sys.argv[1], 'r'))
if cell.atom_velocities.any():
    r_com, v_com = cell.center_of_mass(conv="d", vel=True)
    print "r_com"
    print r_com
    print "v_com"
    print v_com
else:
    r_com = cell.center_of_mass(conv="d")
    print "r_com"
    print r_com
