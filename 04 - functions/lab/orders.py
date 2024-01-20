type_of_product = input()
quantity = int(input())

def calculate(product_type, quantity):
    if product_type == 'coffee':
        price = 1.5 * quantity
    elif product_type == 'water':
        price = 1.0 * quantity
    elif product_type == 'coke':
        price = 1.4 * quantity
    elif product_type == 'snacks':
        price = 2.0 * quantity
    return price


total_price = calculate(type_of_product, quantity)
print(f'{total_price:.2f}')