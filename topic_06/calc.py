import datetime
from operations import get_number, perform_operation

def log_action(data):
    with open("calculator_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {data}\n")

print("--- Калькулятор з логуванням ---")
while True:
    action = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip()
    if action.lower() in ['q', 'й']:
        print("Програму завершено. Логи збережено у calculator_log.txt")
        break
    if action not in ['+', '-', '*', '/']:
        print("Невідома операція.")
        continue
    
    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")
    
    result = perform_operation(action, a, b)
    print(f"Результат: {result}")
    
    log_message = f"Дані: {a}, {b} | Дія: {action} | Результат: {result}"
    log_action(log_message)
    print("-" * 20)