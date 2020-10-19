# adding user input to a dictionary
#creating an empty dictionry
rental_properties = {}
#set a flag to indicate we are taking applications
rental_open = True
while rental_open:
    user_name = input("\n Whats your name?".title())
    rental_address = input("\nwhats the address of the property that you have to rent? ".title())
    #store the response in a dictionary
    rental_properties[user_name] = rental_address
    #ask if the user knows anyone else who might like to rent out their property
    repeat = input("\ndo you know anyone who might like to rent out their property?".title())
    if repeat == 'No':
       rental_open = False
       print("\n ---Property to rent---")
    for user_name,rental_address in rental_properties.items():
       print(user_name + " has " + rental_address + " to rent. ")
