def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Помилка: ділення на нуль!"
    return a / b

while True:
    action = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
    
    if action.lower() == 'q' or action.lower() == 'й':
        print("Програму завершено.")
        break
        
    if action not in ['+', '-', '*', '/']:
        print("Невідома операція. Спробуйте ще раз.")
        continue

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Будь ласка, вводьте лише числа!")
        continue

    match action:
        case "+": print(f"Результат: {add(a, b)}")
        case "-": print(f"Результат: {subtract(a, b)}")
        case "*": print(f"Результат: {multiply(a, b)}")
        case "/": print(f"Результат: {divide(a, b)}")
    print("-" * 20)