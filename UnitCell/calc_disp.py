#!/usr/bin/env python

"""
Calculate the displacement between two unitcells in Cartesian coordinates.

Command-line arguments
----------------------
1) Path to first unitcell to compare
2) Path to second unitcell to compare
3) Whether or not to calculate displacement vectors. If any 3rd argument is
   present, displacement vectors will be calculated, otherwise, only
   displacement magnitudes will be calculated.

"""

import sys

from unitcell import UnitCell, displacements

cell_1 = UnitCell(open(str(sys.argv[1]), 'r'))
cell_2 = UnitCell(open(str(sys.argv[2]), 'r'))

#disp = displacements(cell_1,cell_2,conv='C')
#disp = np.round(disp,decimals=9)
if len(sys.argv) > 2:
    mag, dir_ = displacements(cell_1, cell_2, conv='C', flag=True)
    print mag
    print dir_
else:
    mag = displacements(cell_1, cell_2, conv='C', flag=False)
    print mag
