#using a while loop in a function
def formated_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
while True: 
    print("\n Whats your name?")
    print("\n press q at any time to quit the program ")
    first_name = input("first name : ")
    if first_name == 'q':
        break
    last_name = input("last name : ")
    if last_name == 'q':
        break
    name = formated_name(first_name,last_name)
    print("hello " + name + "!")
