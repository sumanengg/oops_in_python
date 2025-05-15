# Class and Objects
class DOg:
    # Class Attributes
    species = "Canis familiaris"  # Class attribute

    # Constructor
    def __init__(self, name, age, breed):
        # Instance Attributes or variables (unique to each instance)
        # self is a reference to the current instance of the class
        self.name = name  # Instance attribute
        self.age = age
        self.breed = breed
    
    #Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Instance method with class attribute
    def birtday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."
    
    # String representation of the object
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}."
    

dog1 = DOg("Buddy", 3, "Golden Retriever")
dog2 = DOg("Max", 5, "Bulldog")
dog1.species = "Canis lupus familiaris"  # Changing class attribute

# print(dog1.species)  # Output: Buddy says Woof!

# Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner #Public attribute
        self._balance = balance #Protected attribute
        self.__pin = 1234 #Private attribute

    @property
    def get_balance(self):
        return self._balance
    
    @get_balance.setter
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    

# account = BankAccount("Alice", 1000)
# print(account.get_balance)  # Output: 1000
# account.set_balance = -100

# Inheritance

# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."
    def info(self):
        return f"{self.name} is a {self.species}."
    
# Derived class
class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, "Cat")
        self.breed = breed
        self.toy = toy
    
    # Overriding the parent method
    def speak(self):
        return f"Meow!"
    def play(self):
        return f"{self.name} plays with {self.toy}."
    
cat = Cat("Whiskers", "Siamese", "ball")
# print(cat.play())  # Output: Meow!
# print(isinstance(cat, Animal))  # Output: True
# print(Cat.__mro__)

# Abstract Class
# It's a class that cannot be instantiated and is meant to be subclassed.
"""
It's a blueprint for other classes.
1. It's cannot be instantiated directly.
2. Subclasses must implement abstract methods.
3. It can have concrete methods (methods with implementation).

"""
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    def info(self):
        return "This is a shape class."
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    def info(self):
        return "This is a circle class."
    

circle = Circle(5)
print(circle.area())  # Output: 78.5
# shape = shape()  # This will raise an error because shape is an abstract class
