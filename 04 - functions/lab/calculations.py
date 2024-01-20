operator = input()
num1 = int(input())
num2 = int(input())

def calculate(a, b, operator):
    if operator == 'subtract':
        return a - b
    elif operator == 'add':
        return a + b
    elif operator == 'divide':
        return a // b
    elif operator == 'multiply':
        return a * b

print(calculate(num1, num2, operator))
