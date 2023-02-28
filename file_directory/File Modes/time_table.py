#https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy
with open("timetable.txt","w") as tt_file:
  for i in range(2,21):
    for j in range(1,20):
                print(f"{i} times {j} = {i*j}",file=tt_file)
"""
# Time Table
## Instruction
Implement a Python script which creates timetable.txt file in current directory and 
write in the file the timetable from 2 to 20.


### Example Output 

```
2 times 1 = 2
2 times 2 = 4
2 times 3 = 6
2 times 4 = 8
2 times 5 = 10
2 times 6 = 12
2 times 7 = 14
2 times 8 = 16
2 times 9 = 18
2 times 10 = 20
2 times 11 = 22
2 times 12 = 24
2 times 13 = 26
2 times 14 = 28
2 times 15 = 30
2 times 16 = 32
2 times 17 = 34
2 times 18 = 36
2 times 19 = 38
2 times 20 = 40
------------------
3 times 1 = 3
3 times 2 = 6
3 times 3 = 9
3 times 4 = 12
3 times 5 = 15
3 times 6 = 18
3 times 7 = 21
3 times 8 = 24
3 times 9 = 27
3 times 10 = 30
3 times 11 = 33
3 times 12 = 36
3 times 13 = 39
3 times 14 = 42
3 times 15 = 45
3 times 16 = 48
3 times 17 = 51
3 times 18 = 54
3 times 19 = 57
3 times 20 = 60
------------------
4 times 1 = 4
4 times 2 = 8
4 times 3 = 12
4 times 4 = 16
4 times 5 = 20
4 times 6 = 24
4 times 7 = 28
4 times 8 = 32
4 times 9 = 36
4 times 10 = 40
4 times 11 = 44
4 times 12 = 48
4 times 13 = 52
4 times 14 = 56
4 times 15 = 60
4 times 16 = 64
4 times 17 = 68
4 times 18 = 72
4 times 19 = 76
4 times 20 = 80
------------------
5 times 1 = 5
5 times 2 = 10
5 times 3 = 15
5 times 4 = 20
5 times 5 = 25
5 times 6 = 30
5 times 7 = 35
5 times 8 = 40
5 times 9 = 45
5 times 10 = 50
5 times 11 = 55
5 times 12 = 60
5 times 13 = 65
5 times 14 = 70
5 times 15 = 75
5 times 16 = 80
5 times 17 = 85
5 times 18 = 90
5 times 19 = 95
5 times 20 = 100
------------------
6 times 1 = 6
6 times 2 = 12
6 times 3 = 18
6 times 4 = 24
6 times 5 = 30
6 times 6 = 36
6 times 7 = 42
6 times 8 = 48
6 times 9 = 54
6 times 10 = 60
6 times 11 = 66
6 times 12 = 72
6 times 13 = 78
6 times 14 = 84
6 times 15 = 90
6 times 16 = 96
6 times 17 = 102
6 times 18 = 108
6 times 19 = 114
6 times 20 = 120
"""