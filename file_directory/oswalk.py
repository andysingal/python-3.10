#cd ../../
import os

def top_down_walk():
    for dirpath, dirnames, files in os.walk("../../Files"):
        print("Directory: ", dirpath)
        print("-----Include these directories")
        for dirname in dirnames:
            print(dirname)
        print("---Include these files----")
        for file in files:
            print(file)
        print()

top_down_walk()