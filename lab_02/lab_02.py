import sys
import csv

student_list = []

def load_from_csv(filename):
    global student_list
    student_list = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.append({
                    "name": row.get("name", ""),
                    "phone": row.get("phone", ""),
                    "age": row.get("age", ""),
                    "email": row.get("email", "")
                })
        print(f"Дані успішно завантажено з {filename}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створено порожній список.")

def save_to_csv(filename):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ["name", "phone", "age", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student)
    print(f"Дані збережено у {filename}")

def add_student(s_list, name, phone, age, email):
    new_item = {"name": name, "phone": phone, "age": age, "email": email}
    insert_pos = 0
    for item in s_list:
        if name > item["name"]:
            insert_pos += 1
        else:
            break
    s_list.insert(insert_pos, new_item)

def delete_student(s_list, name):
    delete_pos = -1
    for i, item in enumerate(s_list):
        if name == item["name"]:
            delete_pos = i
            break
    if delete_pos != -1:
        del s_list[delete_pos]
        return True
    return False

def update_student(s_list, old_name, new_name, phone, age, email):
    if delete_student(s_list, old_name):
        add_student(s_list, new_name, phone, age, email)
        return True
    return False

def printAllList():
    for elem in student_list:
        print(f"Name: {elem['name']} | Phone: {elem['phone']} | Age: {elem['age']} | Email: {elem['email']}")

def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")
    add_student(student_list, name, phone, age, email)
    print("New element added.")

def deleteElement():
    name = input("Enter name to be deleted: ")
    if delete_student(student_list, name):
        print("Element deleted.")
    else:
        print("Element not found.")

def updateElement():
    name_to_update = input("Enter name to be updated: ")
    found = False
    for item in student_list:
        if item["name"] == name_to_update:
            found = True
            old_phone, old_age, old_email = item["phone"], item["age"], item["email"]
            break
    
    if not found:
        print("Element not found.")
        return
        
    new_name = input(f"New name ({name_to_update}): ") or name_to_update
    new_phone = input(f"New phone ({old_phone}): ") or old_phone
    new_age = input(f"New age ({old_age}): ") or old_age
    new_email = input(f"New email ({old_email}): ") or old_email
    
    update_student(student_list, name_to_update, new_name, new_phone, new_age, new_email)
    print("Element updated.")

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "lab2.csv"
        print(f"Файл не вказано. Використовується файл за замовчуванням: {file_name}")
        
    load_from_csv(file_name)
        
    while True:
        choice = input("\nAction [ C create, U update, D delete, P print, X exit ]: ")
        match choice:
            case "C" | "c": addNewElement()
            case "U" | "u": updateElement()
            case "D" | "d": deleteElement()
            case "P" | "p": printAllList()
            case "X" | "x":
                save_to_csv(file_name)
                print("Exit()")
                break
            case _: print("Wrong choice")

if __name__ == "__main__":
    main()