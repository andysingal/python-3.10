with open('sample.txt','r') as f:
    for line in f:
       line = line.rstrip()
       if line.startswith("Entering"):
            print(line.removeprefix("Entering with"))




