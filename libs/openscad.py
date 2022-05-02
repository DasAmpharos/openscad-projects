import pathlib
import platform
import shutil
import subprocess


class OpenScad:
    def __init__(self):
        binary = shutil.which('openscad')
        if not binary and platform.system() == 'Darwin':
            pass
        if not binary:
            print("'openscad' binary not detected")
            exit(1)
        self.binary = binary
    
    def export_stl(self, filename: str):
        name = pathlib.Path(filename).stem
        subprocess.run([self.binary])
