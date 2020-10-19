prompt = "\n Please enter the name of a book you have read recently."
prompt += "\n to quit type 'q' ."
while True:
    book = input(prompt)
    if book == 'q' :
        break 
    else:
        print("You have recently read " + book.title() + ".")