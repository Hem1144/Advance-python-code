# Constructor
# A constructor is a method that runs automatically when we call a class and this constructor function will target the objects' location.
from abc import abstractmethod, ABC


# class Student:
#     def __init__(self, id, name, age):
#         print(self)
#         # Initialization function and self target the location
#         self.id = id
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")
#
# identity = Student(7, "Joy", 20)
# identity.display()


# Types of Attributes
# Class attribute - A normal variable created inside a class is a class attribute and that's it.
# An Instance attribute - A attribute created using an instance like self.name, self.age etc. It is known as instance attribute.

# Types of Methods
# Instance method - A method that is defined inside a class and is called on an instance of the class.
# Class method - A method that is defined inside a class and is called on the class itself.
# Static method - A method that is defined inside a class but is not bound to the class or the instance.


# Inheritance

# class Parent:
#     x = "I am a Parent class"
#     def display(self):
#         print("I am defined inside the Parent class")
#
# class Child(Parent):
#     pass
    # y = "I am a Child class"
    # def display1(self):
    #     print("I am defined inside the Child class")

# obj = Parent()
# obj1 = Child()
# print(obj.x)
# print(obj1.display())


# Abstract Class

# class AbstractClass(ABC):
#     @abstractmethod
#     def abstract_method(self):
#         pass
#
# class ConcreteClass(AbstractClass):
#     def abstract_method(self):
#         print("Implemented abstract method")
#
# obj = ConcreteClass()
# obj.abstract_method()


# from abc import ABC, abstractmethod
#
#
# class DataIngector(ABC):
#     """
#     Abstract Base Class acting as the contract for all data sources.
#     """
#
#     def __init__(self, source_path: str):
#         self.source_path = source_path
#
#     @abstractmethod
#     def connect(self) -> bool:
#         """Establish connection to the data source."""
#         pass
#
#     @abstractmethod
#     def extract_raw_data(self) -> list[dict]:
#         """Fetch the raw data from the source."""
#         pass
#
#     def clean_data(self, raw_data: list[dict]) -> list[dict]:
#         """
#         A Concrete Method: Shared helper logic.
#         ALL ingestors will clean data the exact same way,
#         so we write the code once here (DRY principle).
#         """
#         print("Standardizing keys and stripping whitespace...")
#         return [{k.lower().strip(): str(v).strip() for k, v in item.items()} for item in raw_data]
#
#
# class CSVIngector(DataIngector):
#
#     def connect(self) -> bool:
#         print(f"Checking if CSV file exists at {self.source_path}...")
#         return True  # Simplified for example
#
#     def extract_raw_data(self) -> list[dict]:
#         print("Parsing CSV file rows...")
#         # Imagine actual CSV parsing logic here
#         return [{" Name ": " Alice ", " Age ": " 30 "}]
#
#
# class APIIngector(DataIngector):
#
#     def connect(self) -> bool:
#         print(f"Pinging REST API endpoint: {self.source_path}...")
#         return True
#
#     def extract_raw_data(self) -> list[dict]:
#         print("Sending GET request and parsing JSON payload...")
#         return [{" Name ": " Bob ", " Age ": " 25 "}]


# from typing import NamedTuple
#
# class User(NamedTuple):
#     name: str
#     age: int
#
# def greet(user: User) -> str:
#     return f"Hello {user.name}, age {user.age}"
#
# print(greet(User("Alice", 30)))


# Multiple Inheritance

# class Father:
#     def skills(self):
#         print("Coding and Safety")
#
# class Mother:
#     def skills(self):
#         print("Cooking and Cleaning")
#
# class Child(Father, Mother):
#     def skills(self):
#         print("Playing, Cooking and Learning")
#
# c1 = Child()
# c1.skills()


# Polymorphism and its types
# 1. Method Overloading === a class has multiple methods with the same name but different parameters.
# 2. Method Overriding  === a child class overrides a method of the parent class.

# 1. Method Overloading

# class Bird:
#     def sound(self):
#         print("Bird can sing a beautiful song")
#
# class Nightingale(Bird):
#     def sound(self):
#         print("Trill & Warble")
#
# bird = Bird()
# bird.sound()
#
# nightingale = Nightingale()
# nightingale.sound()

# 2 Method Overriding

# class Animal:
#     def show(self):
#         print("Animal is showing")
#
# class Human(Animal):
#     def show(self):
#         print("Human is showing")
#
# human = Human()
# human.show()

# Duck Typing

# class Duck:
#     def eat(self):
#         print("eat")
#
# class Dog(Duck):
#     def eat(self):
#         print("eat")
#
# class Cat(Duck):
#     def eat(self):
#         print("eat")
#
# duck = Duck()
# cat = Cat()
# dog = Dog()
# duck.eat()
# cat.eat()
# dog.eat()


# Encapsulation
# It is the process of wrapping data and methods that operate on that data within a single unit, such as a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. In Python, encapsulation is implemented using private and protected access modifiers.

# Access Modifier
# 1. Public: Accessible from anywhere.
# 2. Protected: Accessible within the class and its subclasses. It uses one underscore to represent protected method.
# 3. Private: Accessible only within the class. This is done by using two underscores before the method name.

# Examples

from abc import ABC, abstractmethod
import math


# 1. The Abstract Base Class (The Interface/Contract)
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """
        Calculate and return the area of the shape.
        Every concrete subclass must implement this method.
        """
        pass


# 2. Concrete Subclass: Square
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        # Area of a square: side * side
        return self.side ** 2


# 3. Concrete Subclass: Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        # Area of a circle: pi * r^2
        return math.pi * (self.radius ** 2)

# def print_shape_areas(shapes: list[Shape]) -> None:
#     print(shapes)
#     for shape in shapes:
#         print(type(shape).__name__)
#         print(shape.area())
#         # The type checker and runtime are guaranteed that .area() exists
#         print(f"The area of the {type(shape).__name__} is: {shape.area():.2f}")
#
# # Instantiate your concrete shapes
# shapes_list: list[Shape] = [
#     Square(side=4.0),
#     Circle(radius=3.0)
# ]
#
# print_shape_areas(shapes_list)