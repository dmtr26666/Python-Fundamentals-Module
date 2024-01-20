collection_of_items = input().split("|")
budget = int(input())

items_bought_prices = []
budget_after_selling = 0
profit = 0
NOT_ENOUGH = False

while True:

    for item in collection_of_items:
        current_item = item.split('->')
        item_price = float(current_item[1])

        if (item_price <= budget) and ((current_item[0] == 'Clothes' and item_price <= 50.00) or
                                       (current_item[0] == 'Shoes' and item_price <= 35.00) or
                                       (current_item[0] == 'Accessories' and item_price <= 20.50)):

            budget -= item_price
            profit += item_price * 0.40
            budget_after_selling += item_price * 1.40
            items_bought_prices.append(item_price * 1.40)

    if budget_after_selling + budget < 150:
        NOT_ENOUGH = True
        break
    else:
        break

for price in items_bought_prices:
    print(f"{price:.2f}", end=' ')

print()
print(f'Profit: {profit:.2f}')

if NOT_ENOUGH:
    print("Not enough money.")
else:
    print("Hello, France!")