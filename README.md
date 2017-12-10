UnitCell
========

Python class, functions, and scripts to create, store, and manipulate 
crystallographic unit cell data.

The UnitCell class in unitcell.py does all of the heavy lifting.
Other scripts in the package use the UnitCell class to convert unit cell files
from one format to another or perform specific tasks on a unit cell.

File-Format Conversions
-----------------------
- atat_to_vasp : Converts 
    [ATAT](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/) 
    formatted file to [VASP](https://www.vasp.at/) 4 format.
- gulp_output_to_vasp : Converts [GULP](http://gulp.curtin.edu.au/gulp/) 
    formatted output file to VASP 4 format.
- gulp_to_gulp : Converts GULP output format to GULP input format.
- vasp_to_findsym : Converts VASP format (4 or 5) to findsym format.
- vasp_to_gulp : Converts VASP format (4 or 5) to GULP input format.
- vasp_to_lammps : Converts VASP format (4 or 5) to LAMMPS input format.  
    This conversion requires the unitcell to be orthogonal and the unit cell 
    parameter matrix to be diagonal.

Unit Cell Manipulations
-----------------------
This package can be used to calculate quantitites related to a unit cell and
manipulate parameters of a unit cell:
- Calculate the center of mass of atoms in the cell
- Displace all atoms in the unit cell by specified amounts
- Calculate reciprocal-space lattice vectors of the cell
- Calculate k-point mesh corresponding to a desired KPPRA 
    (with several caveats, see kmesh.py for details).
- Calculate the electrostatic potential alignment between two point defect 
    calculations or a point defect calculation and the perfect crystal 
    calculation. This electrostatic potential alignment was used in
    [Doak, Michel, & Wolverton, J. Mater. Chem. C 3, 10630–10649 (2015)](http://xlink.rsc.org/?DOI=C5TC02252E).
- Calculate the space group of a crystal. Space group calculations require the 
    findsym software, part of the 
    [isotropy software suite](http://stokes.byu.edu/iso/isolinux.php).
