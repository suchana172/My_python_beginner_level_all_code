
stock_items = []
#make 50 blue pens 

for blue in range(0,50):
    new_blue_pen = {'color': 'blue','type':'ballpoint','price':'10$'}
    stock_items.append(new_blue_pen)
#changing the price of the 1st 5 pens

for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '10$':
        blue_pen['price'] = '9$'
for blue_pen in stock_items[0:5]:
    print(blue_pen)

