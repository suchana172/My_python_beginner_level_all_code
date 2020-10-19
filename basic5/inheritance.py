"""Inheritance"""
#creating a new ereader class
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

class KindleFire(Ereader):  #child class
    # Represents aspects of an ereader specific to a kindle fire.then initialize attributes specific to a kindle fire.
    def __init__(self,make,model,backlight,battery,screen_type,screen_resolution = '1200*180'):
        #initialize attributes for a kindle fire
        self.screen_resolution = screen_resolution

        super().__init__(make,model,backlight,battery,screen_type)
    def describe_screen(self):
        #print out some marketing copy about kindle fire
        print("Fire Hd 8 is a widescreen " + self.screen_resolution + " HD screen")

my_kindle_fire = KindleFire('Amazon','kindle fire','backlight','12 hour battery life','color screen')
print(my_kindle_fire.get_ereader_name())
my_kindle_fire.describe_screen()




