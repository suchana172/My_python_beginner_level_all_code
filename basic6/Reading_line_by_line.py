#Reading a file line by line 

file_name = 'movies_line_by_line.txt'
with open(file_name) as file_object:
    for line in file_object:
        print("\n" + line)