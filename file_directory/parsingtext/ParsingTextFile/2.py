def number_of_characters(file_path):
    with open(file_path) as file:
        for index, row in enumerate(file,start=1):
            print(f"Line:{index}-{len(row)} characters")

number_of_characters("pythonwiki.txt")