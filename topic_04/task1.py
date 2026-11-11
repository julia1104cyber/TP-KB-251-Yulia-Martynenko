def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено не число! Будь ласка, спробуйте ще раз.")

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: неможливо поділити на нуль!"

while True:
    action = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
    
    if action.lower() == 'q' or action.lower() == 'й':
        print("Програму завершено.")
        break
        
    if action not in ['+', '-', '*', '/']:
        print("Невідома операція. Спробуйте ще раз.")
        continue

    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")

    match action:
        case "+": print(f"Результат: {add(a, b)}")
        case "-": print(f"Результат: {subtract(a, b)}")
        case "*": print(f"Результат: {multiply(a, b)}")
        case "/": print(f"Результат: {divide(a, b)}")
    print("-" * 20)