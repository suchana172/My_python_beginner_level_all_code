#passing a list to a function
def books_available(books):
    for book in books:
        books_in_stock = "The following books are available to buy " + book
        print(books_in_stock)
available = ['the X','the Y','the Z']
books_available(available)
