#using a flag to stop program 
prompt = "\n Enter 'q' to end this program "
prompt += "\n Whats your name ?"
#set our flag to true
active = True
while active :
    message = (input(prompt))
    if message == 'q':
        active = False
    else:
        print(message)
