class Caretaker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Caretaker'

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"