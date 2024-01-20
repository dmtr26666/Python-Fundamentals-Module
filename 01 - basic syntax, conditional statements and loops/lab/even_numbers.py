numbers = int(input())
ALERT = False


for i in range(numbers):
    number = int(input())

    if number % 2 != 0:
        print(f'{number} is odd!')
        ALERT = True
        break

if not ALERT:
    print('All numbers are even.')
