# The   else block
print("Enter two number to be divided ")
print("\n Enter q to quit .")
while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second number : ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by zero .")
    else:
        print(answer)
    
    
    