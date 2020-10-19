# working with multiple files
def word_count(filename):
    # Count the number of files in a word
    try:
       with open(filename) as file_object :
           contents = file_object.read()
    except FileNotFoundError:
        pass 
       #message = "Sorry, this file " + filename + " cannot found "
       #print(message)
    else:
       words = contents.split()
       number_words = len(words)
       print("The file " + filename + " has approximately " + str(number_words) + " words")
filenames = ['heathcliff.txt','mobydick.txt']
for filename in filenames:
    word_count(filename)