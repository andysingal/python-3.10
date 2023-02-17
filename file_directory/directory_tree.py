import pathlib

def display_tree():
    directory = pathlib.Path.cwd()
    print(f"+ {directory}")
    entries = directory.rglob("*")
    for entry in entries:
              depth = len(entry.relative_to(directory).parts)
              spacer = '    ' * depth
              print(f"{spacer}+ {entry.name}")

#
#
display_tree()
# root = pathlib.Path.cwd()
# child_path = pathlib.Path("/Users/ankush.singal/PycharmProjects/pythonProject9/delab-venv/bin")
# print(child_path)