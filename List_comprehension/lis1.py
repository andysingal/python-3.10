# list = [1,1,2,3,5,8,13,21,34,55]
# nomi = [el ** 2  for el in list]
# print(nomi, end=" ")

with open("file1.txt",'r') as f:
    content = f.readlines()
with open("file2.txt",'r') as f:
    content2 = f.readlines()

result = [int(num) for num in content if num in content2]
print(result)
