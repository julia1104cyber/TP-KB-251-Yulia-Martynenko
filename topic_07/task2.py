class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

students = [
    Student("Олена", 20),
    Student("Іван", 19),
    Student("Марія", 22),
    Student("Андрій", 18)
]

print("--- Відсортовано за віком (зростання) ---")
sorted_by_age = sorted(students, key=lambda s: s.age)
for student in sorted_by_age:
    print(student)

print("\n--- Відсортовано за ім'ям (алфавіт) ---")
sorted_by_name = sorted(students, key=lambda s: s.name)
for student in sorted_by_name:
    print(student)