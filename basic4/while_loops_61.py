#working with while lops & lits
unconfirmed_users = [ 'suchana','santona','bornil']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying user: " + current_user.title() )
    confirmed_users.append(current_user)
    #display all confirmed users
    print("\n The following users have been confirmed : ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
