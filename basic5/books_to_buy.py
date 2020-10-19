#our module / importing an entire module
def books_available(*books):
    #show a list of books available to buy
    for book in books:
        books_in_stock = "The following books are available to buy " +book
        print(books_in_stock)
def books_description(author_name,book_type = 'science_fiction'):
    print(" this is a " + book_type + " book.")
    print("the author of the book is " + author_name.title())
