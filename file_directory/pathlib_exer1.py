import pathlib

from pathlib import Path
from datetime import datetime
#Implement a Python function which takes a path as a parameter
# and return the last modified file or folder in the given path
def find_last_modified(directory):
    time=0
    result_file = pathlib.Path(".")
    entries = directory.iterdir()
    for entry in entries:
        meta_data = entry.stat()
        if time <  meta_data.st_mtime:
            time = meta_data.st_mtime
            result_file = entry.name
    return f"Date modified:  {datetime.fromtimestamp(time)}, Filename: {result_file}"




directory = Path.cwd()
print(find_last_modified(directory))