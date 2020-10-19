#modifying a list in a function
def passengers(not_checked_in,checked_in):

    #simulate passergers who are not checked in
    while not_checked_in:
        #simulte checking a passenger in
        current_passenger = not_checked_in.pop()
        print("checking a passenger " + current_passenger)
        checked_in.append(current_passenger)
def show_checked_in_passengers(checked_in):
    #show all the passengers who have checked in
    print("\The following passengers have been checked in ")
    for passengers in checked_in:
        print(passengers)
not_checked_in =['Suchan Suchi','santona sadat','bornil','biplob']
checked_in = []
passengers(not_checked_in,checked_in)
show_checked_in_passengers(checked_in)
