from math import ceil

budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_eggs = float(input())
price_for_apron = float(input())

free_flour = students // 5

total_price = price_for_flour * (students - free_flour) + (price_for_eggs * 10) * students + price_for_apron * (ceil(students * 1.2))


if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")



