#working with acontent of a file

filename = 'movies_line_by_line.txt'
with open(filename) as file_object :
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
    print("\n---------------------------------\n")
    poped_movies = lines.pop() #last er movie information delete hobe
    for line in lines:
        print(line.strip())
    print("\n***********************************\n")
    sorted_list = lines.sort()
    for line in lines:
        print(line.strip())