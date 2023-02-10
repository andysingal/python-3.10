import os
from datetime import datetime


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formatted_date


def display_cwd():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")


# def display_entries_in_directory(directory):
#     # os.list
#     entries = os.scandir(directory)
#     for entry in entries:
#         info = entry.stat()
#         print(f"{entry.name} Creation_date: {format_datetime(info.st_birthtime)}")
#         #creation data info.st_ctime
#         print (f"{entry.name} Access_date: {format_datetime (info.st_atime)}")
#         print (f"{entry.name} Access_date: {format_datetime (info.st_size)}")
def display_directories(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_dir():
            print (f"Directory name: {entry.name}")

def display_files(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_file():
            print(f"File name: {entry.name}")


display_cwd()
os.chdir("../../")
display_cwd()
display_directories('./')
# display_entries_in_directory("./")
display_files('./')