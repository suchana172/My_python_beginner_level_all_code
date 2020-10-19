#using positional & arbitraty arguments together
def assign_seat(seat,*requests):
    #assign a seat & request to a passenger
    print("Assign seat number " + str(seat) + " The following passenger request. ")
    for request in requests:
        print("-" + request)
assign_seat(29,'window seat')