from pathlib import Path
# def display_directory_content():
#     entries = Path.cwd()
#     for entry in entries.iterdir():
#         print (f"File name: {entry.name}")
#         print (f"File Directory: {entry.parent}")
#         print (f"File name without extension: {entry.stem}")
#         print (f"File  extension: {entry.suffix}")
#         print()
#
def display_directory_content():
    path = Path.cwd()
    file_names = path.glob('*.py')
    #filenames = path.glob("**/*.txt")
    for file_name in file_names:
        print(file_name.stem)
        print (file_name.suffix)
        print (file_name.parent)
        print()
print(display_directory_content())