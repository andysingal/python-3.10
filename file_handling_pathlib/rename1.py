from pathlib import Path

# root_dir = Path('sample_files')
#
# for path in root_dir.glob("**/*"):
#   if path.is_file():
#       parent_folder = path.name
#       new_filepath = path.with_name(parent_folder)
#       print(new_filepath)

def rename_file(file_name, new_name, file_type):
    current_path = Path.cwd()
    for item in current_path.iterdir():
        if item.is_file() and item.suffix == file_type:
            if item.stem == file_name:
              update_name = new_name + file_type
              item.rename(update_name)

rename_file('file1','test','.txt')

