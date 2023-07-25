# This is a multifunction calculator built with Python

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


num1 = float(input("Enter first number: "))
for symbol in operators:
    print(symbol)
symbol = input('Enter symbol from above: ')
num2 = float(input("Enter second number: "))

calculate_operation = operators[symbol]

answer = calculate_operation(num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")
