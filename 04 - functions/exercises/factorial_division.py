def factorial(number1, number2):
    num1_factorial = 1
    num2_factorial = 1

    for num in range(2, number1 + 1):
        num1_factorial *= num

    for num in range(2, number2 + 1):
        num2_factorial *= num

    result = num1_factorial / num2_factorial
    print(f"{result:.2f}")


num1 = int(input())
num2 = int(input())
factorial(num1, num2)

