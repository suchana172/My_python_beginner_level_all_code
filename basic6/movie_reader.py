# Reading entire file
with open('movie.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())
