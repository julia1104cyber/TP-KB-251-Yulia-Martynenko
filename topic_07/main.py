from calc_class import Calculator

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено не число!")

def run_calculator():
    calc = Calculator() 
    print("--- ООП Калькулятор ---")
    
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
        
        match action:
            case "+": result = calc.add(a, b)
            case "-": result = calc.subtract(a, b)
            case "*": result = calc.multiply(a, b)
            case "/": result = calc.divide(a, b)
        
        print(f"Результат: {result}")
        print("-" * 20)

if __name__ == "__main__":
    run_calculator()