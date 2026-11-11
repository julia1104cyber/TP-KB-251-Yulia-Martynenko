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

def calculator_match(a, b, operation):
    match operation:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)
        case _:
            return "Невідома операція"

print("10 * 5 =", calculator_match(10, 5, "*"))
print("10 - 5 =", calculator_match(10, 5, "-"))