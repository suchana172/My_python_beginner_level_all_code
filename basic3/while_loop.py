 #using while loop to quit a program 
prompt = "\nto end this program enter 'q'."
prompt += "\nPlease enter your name : "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)