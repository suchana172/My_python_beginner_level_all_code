from test_function_1 import get_formated_name
print("Enter q to quit : ")
while True:
    first = input("What is your firstname? ")
    if first == 'q':
        break
    last = input("What is your last name? ")
    if last == 'q':
        break
    formated_name = get_formated_name(first,last)
    print( " Your name is " + formated_name + ".")
