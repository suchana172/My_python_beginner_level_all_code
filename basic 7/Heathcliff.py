#Analyzing text
filename = 'heathcliff.txt'
try:
    with open(filename) as file_object :
        contents = file_object.read()
except FileNotFoundError:
    message = "Sorry, this file " + filename + " cannot found "
    print(message)
else:
    words = contents.split()
    number_words = len(words)
    print("The file " + "has approximately " + filename + str(number_words) + "words")
