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
