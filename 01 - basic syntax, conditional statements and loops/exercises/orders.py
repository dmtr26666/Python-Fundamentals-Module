number_of_orders = int(input())

total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100 or days < 1 or days > 31 or \
            capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    price_for_order = (days * capsules_needed_per_day) * price_per_capsule
    total_price += price_for_order
    print(f"The price for the coffee is: ${price_for_order:.2f}")


print(f"Total: ${total_price:.2f}")
