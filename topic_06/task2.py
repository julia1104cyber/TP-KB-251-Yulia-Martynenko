students = [
    {"name": "Олена", "grade": 95},
    {"name": "Іван", "grade": 75},
    {"name": "Марія", "grade": 88},
    {"name": "Андрій", "grade": 92}
]

print("--- Початковий список ---")
for s in students: 
    print(s)

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("\n--- Відсортовано за ім'ям ---")
for s in sorted_by_name: 
    print(s)

sorted_by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\n--- Відсортовано за оцінкою (від найвищої) ---")
for s in sorted_by_grade: 
    print(s)