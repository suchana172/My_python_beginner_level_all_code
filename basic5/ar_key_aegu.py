#using arbitraty keyword arguments
def seat_profile(first,last,**passenger_info):
    #build a dictionary containing all passengers info
    profile = {}
    profile['first_name'] = first
    profile['last_name ']= last
    for key,value in passenger_info.items():
        profile[key]=value
    return profile
passengers_profile = seat_profile('suchana','suchi',seat_number=29,pre_ordered_breakfast='yes')
print(passengers_profile)