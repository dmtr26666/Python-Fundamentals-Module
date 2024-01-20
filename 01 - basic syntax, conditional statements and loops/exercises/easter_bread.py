budget = float(input())
price_for_1kg_flour = float(input())

price_for_1_pack_eggs = price_for_1kg_flour * 0.75
price_for_1_liter_milk = price_for_1kg_flour * 1.25

price_for_bread = price_for_1kg_flour + price_for_1_pack_eggs + price_for_1_liter_milk * 0.25

bread_counter = 0
eggs_counter = 0

while True:
    if budget < price_for_bread:
        break

    bread_counter += 1
    eggs_counter += 3
    budget -= price_for_bread

    if bread_counter % 3 == 0:
        eggs_counter -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")