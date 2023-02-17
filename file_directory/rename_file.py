import pathlib

#Condition for only files and selected types
#Check if the file exists in cwd
#if exists rename to new name
def rename_file(file_name,new_name,file_type):
    current_path = pathlib.Path.cwd ()
    for item in current_path.iterdir():
        if item.is_file() and item.suffix == file_type:
            if item.stem == file_name:
                  update_name = new_name + file_type
                  item.rename(update_name)
                  print(f"File name is successfully change from {file_name+file_type} to {update_name}")
                  return
    print(f"The file {file_name+file_type} does not exist")
rename_file('test1','applemillers','.txt')