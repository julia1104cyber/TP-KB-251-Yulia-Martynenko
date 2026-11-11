def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def calculator_if_else(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Невідома операція"

print("10 + 5 =", calculator_if_else(10, 5, "+"))
print("10 / 0 =", calculator_if_else(10, 0, "/"))