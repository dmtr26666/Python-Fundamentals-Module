items = {}

while True:
    item = input()
    if item == 'buy':
        break

    name, price, quantity = item.split()

    if name in items.keys():
        items[name]['price'] = float(price)
        items[name]['quantity'] += float(quantity)

    else:
        items[name] = {'price': float(price), 'quantity': float(quantity)}

for item, value in items.items():
    print(f"{item} -> {value['price'] * value['quantity']:.2f}")