#File not found error
filename = 'suchana.txt'
try:
   with open(filename) as object_file:
    content = object_file.read()
except FileNotFoundError:
    message = "Sorry, The file " + filename + " cannot be found"
    print(message)