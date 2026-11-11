from functions import add, subtract, multiply, divide

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено не число!")

def perform_operation(action, a, b):
    match action:
        case "+": return add(a, b)
        case "-": return subtract(a, b)
        case "*": return multiply(a, b)
        case "/": return divide(a, b)