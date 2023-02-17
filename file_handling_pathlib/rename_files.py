from pathlib import Path

root_dir= Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        # path.rename(new_filepath)

"""from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    parent_folder = path.parts
    subfolders = path.parts[1:-1]

    new_filename = "-".join(subfolders) + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
"""


"""
December-def.txt
December-ghi.txt
November-abc.txt
November-jkl.txt
"""
