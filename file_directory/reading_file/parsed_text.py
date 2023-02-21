def number_of_lines_file():
    file_name = input("Enter the file name: ")
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("Please enter correct file name")
        exit()
    word = input("Enter the word: ")
    line_count = 0
    for line in file:
        line = line.rstrip()
        if line.startswith(word):
            print(line)
            line_count+= 1
    print(f"There are {line_count} {word} in {file_name}")

number_of_lines_file()