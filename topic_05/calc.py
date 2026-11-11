from operations import get_number, perform_operation

print("--- Модульний Калькулятор ---")
while True:
    action = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip()
    if action.lower() in ['q', 'й']:
        print("Програму завершено.")
        break
    if action not in ['+', '-', '*', '/']:
        print("Невідома операція.")
        continue
    
    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")
    
    result = perform_operation(action, a, b)
    print(f"Результат: {result}")
    print("-" * 20)