import os

print(os.getcwd())
path = os.path.join("folder1","folder2","folder3","logo.png")

path1 = os.path.basename('/Users/ankush.singal/PycharmProjects/pythonProject9/file_directory/os_module.py')
# print(path1)

path2 = os.path.exists('/Users/ankush.singal/PycharmProjects/pythonProject9/file_directory/os_module.py')
# print(path2)

path3 = os.path.isdir('/Users/ankush.singal/PycharmProjects/pythonProject9/file_directory/os_module.py')
# print(path3)

path4 = os.path.getsize('/Users/ankush.singal/PycharmProjects/pythonProject9/file_directory/os_module.py')
# print(path4)

#Count the number of files
def display_files(directory):
    entries = os.scandir(directory)
    total = 0
    for entry in entries:
        if entry.is_file ():
            print(entry.name)
            total += 1
    print(total)

print(display_files('./'))

