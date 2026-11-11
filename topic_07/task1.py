class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Людина (Ім'я: {self.name}, Вік: {self.age})"

person1 = Person("Юлія", 19)

print(person1)