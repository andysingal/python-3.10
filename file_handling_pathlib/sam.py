from pathlib import Path

p1 = Path('abc.txt')
print(type(p1))
if p1.exists():
    with open('abc.txt','r') as file:
            print(file.read())

print(p1.name)
print(p1.suffix)
print(p1.stem)

p2= Path('/Users/ankush.singal/PycharmProjects/pythonProject9/file_handling_pathlib')
file_paths = p2.iterdir()
# print(list(file_paths))

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)


