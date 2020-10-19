#checking if a value is not in a list
admin_user =['suchana','santona']
username = input("please enter an username :")
if username not in admin_user:
    print("You do not have to access")
else:
    print("access granted ")