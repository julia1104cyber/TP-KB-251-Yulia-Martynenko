import requests

def get_currency_rate(currency_code):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        data = response.json()
        for item in data:
            if item['cc'] == currency_code:
                return item['rate']
        return None
    except:
        print("Помилка з'єднання з API НБУ.")
        return None

print("Доступні валюти для конвертації: EUR, USD, PLN")
currency = input("Введіть тип валюти: ").upper().strip()

if currency in ["EUR", "USD", "PLN"]:
    try:
        amount = float(input("Введіть кількість валюти: "))
        rate = get_currency_rate(currency)
        if rate:
            result = amount * rate
            print(f"Поточний курс {currency}: {rate}")
            print(f"{amount} {currency} = {result:.2f} UAH")
        else:
            print("Не вдалося знайти курс для цієї валюти.")
    except ValueError:
        print("Помилка: введіть числове значення!")
else:
    print("Помилка: ця валюта не підтримується.")