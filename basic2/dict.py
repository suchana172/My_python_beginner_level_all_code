###using a list within  a dictionary

#store information about a car we want to bye

my_ordered_car = {
    'type': 'standard foor door saloon',
    'extras': ['alloy wheels','climate control','leather heated seats'],
}
#print order summary
print("the car you ordered is a " + my_ordered_car['type'] + " with the following extras :")
for extra in my_ordered_car['extras']:
    print("\t" + extra)

