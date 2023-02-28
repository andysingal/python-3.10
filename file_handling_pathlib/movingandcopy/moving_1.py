import shutil,os

# shutil.copy('Documents/instructions.txt', 'Data')
#
# # shutil.copytree('Data' , 'Documents/Data2')
# os.chdir('Data')
# print(os.getcwd())
# os.unlink('instructions.txt')

# os.rmdir()
# shutil.rmtree()

os.chdir('Documents/Data2')
for film_name in os.listdir():
    if film_name.endswith('.txt'):
        # print(film_name)
        os.unlink(film_name)
