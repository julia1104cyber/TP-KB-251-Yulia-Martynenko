my_dict = {"name": "Yulia", "age": 19}
print("Початковий словник:", my_dict)

my_dict.update({"city": "Chernihiv", "student": True})
print("Після update:", my_dict)

del my_dict["student"]
print("Після del (видалення ключа 'student'):", my_dict)

print("Ключі (keys):", list(my_dict.keys()))
print("Значення (values):", list(my_dict.values()))
print("Елементи (items):", list(my_dict.items()))

my_dict.clear()
print("Після clear():", my_dict)