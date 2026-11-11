my_list = [10, 20, 30]
print("Початковий список:", my_list)

my_list.append(40)
print("Після append(40):", my_list)

my_list.extend([50, 60])
print("Після extend([50, 60]):", my_list)

my_list.insert(1, 15)
print("Після insert(1, 15):", my_list)

my_list.remove(15)
print("Після remove(15):", my_list)

my_list.sort(reverse=True)
print("Після sort(reverse=True):", my_list)

my_list.reverse()
print("Після reverse():", my_list)

list_copy = my_list.copy()
print("Скопійований список (copy):", list_copy)

my_list.clear()
print("Після clear():", my_list)