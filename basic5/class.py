#creating our first class
class book():
    def __init__(self,name,price,publisher):
        self.name = name
        self.price = price 
        self.publisher = publisher
    def hardback(self):   #simulate a hardback book
        print(self.name.title() + " is a hardback book")
    def softback(self):  # simulate a book being softback
        print(self.name.title() + " is a softback book ")
    def ebook(self): # simulate a book called ebook
        print(self.name.title() + " is a ebook ")
    def ebook_reader(self):  # simulate an ebook reader
        print("Library :" + self.name.title() + " , " +str(self.price) + " , " + self.publisher.title())
# Creating an instance of our book class

my_book = book('elon musk',15,'virgin books') 
your_book = book('the firms',11,'virgin books')

#Accessing attributes
"""print("I am currently reading " + my_book.name.title() + ".")
print("This book cost $ " + str(my_book.price) + ".")
my_book.softback()
my_book.hardback()""" 

#calling our ebook reader method
my_book.ebook_reader()
your_book.hardback()





