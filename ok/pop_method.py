subcribers = ['suchana@example.com','santona@example.com','biplob@example.com']
print(subcribers)
poped_subcriber = subcribers.pop()
print(subcribers)
print(poped_subcriber)
subcribers = ['suchana@example.com','santona@example.com','biplob@example.com']
first_subcriber = subcribers.pop(0)
print(first_subcriber)
subcribers = ['suchana@example.com','santona@example.com','biplob@example.com']
print(subcribers)
subcribers.remove('santona@example.com')
print(subcribers)
subcribers = ['suchana@example.com','santona@example.com','biplob@example.com']
subcriber_by_mistake = ('biplob@example.com')
subcribers.remove(subcriber_by_mistake)
print(subcribers)
print("\n this person " + subcriber_by_mistake + " did not mean to sign up")
