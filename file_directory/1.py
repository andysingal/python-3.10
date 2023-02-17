import os

def display_cwd():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")


def up_one_directory_level():
    os.chdir("../")
#
#
def display_entries_in_directory(directory):
    entries = os.scandir(directory)
    for entry in entries:
        print(entry.name)
#
#
display_cwd()
up_one_directory_level()
up_one_directory_level()
display_cwd()
display_entries_in_directory("../")

# # Import Module
# import os
#
# # Folder Path
# path = "/content/nomi"
#
# # Change the directory
# os.chdir (path)
#
# # Get the current working
# # directory (CWD)
# cwd = os.getcwd ()
#
# # Print the current working
# # directory (CWD)
# print ("Current working directory:", cwd)
#
#
# def read_files(file_path):
#     with open (file_path, 'r') as file:
#         print (file.read ())
#
#
# # Iterate over all the files in the directory
# for file in os.listdir ():
#     if file.endswith ('.txt'):
#         # Create the filepath of particular file
#         file_path = f"{path}/{file}"
#
# read_files (file_path)
# print ("\n")