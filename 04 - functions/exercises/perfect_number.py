def devisors(number):
    list_of_devisors = [num for num in range(1, number) if number % num == 0]

    return list_of_devisors

number = int(input())
result = devisors(number)

if sum(result) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
