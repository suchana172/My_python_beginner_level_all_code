#Writing multiple lines to a file & using append
message = input("What is your favourite film? ")
print(message.title())
filename = 'favourite_film.txt'
with open(filename,'a') as file_object:   #here 'a' for append
    file_object.write(message + "\n")