#!/usr/bin/env python

"""
kmesh.py Jeff Doak jeff.w.doak@gmail.com

Calculate the k-point mesh along reciprocal lattice vectors that will give a
specified k-points per reciprocal atom (KPPRA).

Does not account for offset of origin of k-point mesh.
Does not try to keep mesh dimensions even or odd.

"""

import sys

import numpy as np

from unitcell import UnitCell

# Read in crystal structure and desired kppra
if len(sys.argv) > 2:
    poscar = UnitCell(str(sys.argv[1]))
    KPPRA = int(sys.argv[2])
else:
    poscar = UnitCell("POSCAR")
    KPPRA = int(sys.argv[1])

# Calculate relative magnitudes of reciprocal lattice vectors
recip = poscar.recip_lat()
b1 = np.linalg.norm(recip[0])
b2 = np.linalg.norm(recip[1])
b3 = np.linalg.norm(recip[2])
b2 = b2/b1
b3 = b3/b1
b1 = 1.0

# Determine scale factor which will give desired KPPRA
scale = 1
while True:
    kx = int(np.floor(scale*b1))
    ky = int(np.floor(scale*b2))
    kz = int(np.floor(scale*b3))
    kppra = poscar.num_atoms*kx*ky*kz
    if kppra >= KPPRA:
        break
    scale += 1

# Output K-point mesh that gives desired KPPRA
print kx, ky, kz
sys.exit()
