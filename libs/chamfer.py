import os

import solid

__script_dir = os.path.dirname(os.path.abspath(__file__))

# chamfer.scad
__library_path = os.path.join(__script_dir, 'chamfer.scad')
chamfer = solid.import_scad(__library_path)