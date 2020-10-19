#A class that represents a basic ereader

class Ereader():   #a class to represent a ereader parent class
    def __init__(self,make,model,backlight,battery,screen_type): #initialixe the attributes to discribe an ereader
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count =0   # setting default value using this
    def get_ereader_name(self):
        #return a formated descriptive name for aour ereader
        long_name = self.make + " - " + self.model + " - " + self.backlight + " -" + self.battery + " - " + self.screen_type
        return long_name.title()
    def read_library_count(self):
        #show the amount of ebooks in our kindle library
        print("you have " +str(self.library_count) + " books in kindle library. ")
    def update_library_count(self,ebook_count):
        #update a library count
        self.library_count = ebook_count
    def increment_library_count(self,puchased_ebooks):
        #add our new ebooks to library count
        self.library_count += puchased_ebooks    # + deya hoyeche cz increment