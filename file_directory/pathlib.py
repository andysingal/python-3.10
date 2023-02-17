# import os,glob,shutil
#
# for file_name in glob.glob('*.txt'):
#     new_path = os.path.join("archive",file_name)
#     shutil.move(file_name,new_path)
from pathlib import Path
path_test = Path.cwd() /"test.txt"
print(f"File name: {path_test.name}")
print(f"File Directory: {path_test.parent}")
print(f"Parent File Directory: {path_test.parent.parent}")
print(f"File name without extension: {path_test.stem}")
print(f"File  extension: {path_test.suffix}")
print(Path.home().joinpath("new folder","test","appellers"))