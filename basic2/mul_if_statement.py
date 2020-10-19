shopping_cart = ['pen','pencil','book']

for item in shopping_cart:
    if item == 'pen':
        print("sorry this item is out of stock")
    else:
        print("adding " + item + " to your order")
print("your order is complete ")
# for empty shopping cart 
shopping_cart =[]
if shopping_cart:
    for item in shopping_cart:
        print("your order is complete")
    print("adding " + item + " to your cart")
else:
    print("you must select a item before proceeding")