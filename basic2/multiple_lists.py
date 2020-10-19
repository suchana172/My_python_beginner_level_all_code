in_stock = ['banana','pen','pencil','book']
shopping_cart = ['banana','pen','pencil','book','mango']
for item in shopping_cart:
    if item in in_stock:
        print("adding " + item + " to your order")
    else:
        print("sorry, " + item + " is not in stock")
print("your order is complete")

