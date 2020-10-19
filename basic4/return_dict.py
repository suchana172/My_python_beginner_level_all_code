#returning dictionary
def build_book(name,author,publisher):
    my_book = { 'name': name,'author':author, 'publisher':publisher}
    return my_book
book = build_book('english','james','academy')
print(book)
