def create_passenger(*requests):
    print(requests)
create_passenger('window seat','seat near top of the plane','pre order breakfast')
#arbitrary arguments 2
def create_passengers(*requests):
    print("\nThis passenger has requested :")
    for request in requests:
        print("-" + request)
create_passengers('window seat','seat near top of the plane','pre order breakfast') 
