# Constructor
# A constructor is a method that runs automatically when we call a class and this constructor function will target the objects' location.

class Student:
    def __init__(self, id, name, age):
        print(self)
        # Initialization function and self target the location
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")

identity = Student(7, "Joy", 20)
identity.display()




