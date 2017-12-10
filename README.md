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

Space group calculations require the findsym software, part of the 
[isotropy software suite](http://stokes.byu.edu/iso/isolinux.php).
