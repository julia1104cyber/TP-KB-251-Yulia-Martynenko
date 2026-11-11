def find_insert_position(sorted_list, new_element):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= new_element:
            return i
    return len(sorted_list)

my_list = [10, 20, 30, 40, 50]
new_val = 35

pos = find_insert_position(my_list, new_val)

print(f"Відсортований список: {my_list}")
print(f"Нове значення для вставки: {new_val}")
print(f"Позиція (індекс) для вставки: {pos}")

my_list.insert(pos, new_val)
print(f"Список після вставки: {my_list}")