student_list = [
    {"name":"Bob",  "phone":"0631234567", "age": 19, "email": "bob@test.com"},
    {"name":"Emma", "phone":"0631234567", "age": 22, "email": "emma@test.com"},
    {"name":"Jon",  "phone":"0631234567", "age": 21, "email": "jon@test.com"},
    {"name":"Zak",  "phone":"0631234567", "age": 18, "email": "zak@test.com"}
]

def printAllList():
    for elem in student_list:
        strForPrint = (f"Student name is {elem['name']}, Phone is {elem['phone']}, "
                       f"Age is {elem['age']}, Email is {elem['email']}")
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    
    newItem = {"name": name, "phone": phone, "age": age, "email": email}
    
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del student_list[deletePosition]
    return

def updateElement():
    name_to_update = input("Please enter name to be updated: ")
    
    updatePosition = -1
    for i, item in enumerate(student_list):
        if item["name"] == name_to_update:
            updatePosition = i
            break

    if updatePosition == -1:
        print("Element was not found")
        return

    print("Enter new data (or leave empty to keep current):")
    new_name = input(f"New name ({student_list[updatePosition]['name']}): ") or student_list[updatePosition]['name']
    new_phone = input(f"New phone ({student_list[updatePosition]['phone']}): ") or student_list[updatePosition]['phone']
    new_age = input(f"New age ({student_list[updatePosition]['age']}): ") or student_list[updatePosition]['age']
    new_email = input(f"New email ({student_list[updatePosition]['email']}): ") or student_list[updatePosition]['email']

    del student_list[updatePosition]

    updatedItem = {"name": new_name, "phone": new_phone, "age": new_age, "email": new_email}

    insertPosition = 0
    for item in student_list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
            
    student_list.insert(insertPosition, updatedItem)
    print("Element has been updated")

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()