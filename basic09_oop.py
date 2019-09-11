"""
Documentation here
"""
# ------------------------- modules training -------------------------
# -------------------------------------------------------------------
# import a function from a module
from basic0 import head
from basic0 import comment
from basic0 import title
#from basic0 import qoute_str
from basic0 import sep

#-------------------------- OOP training --------------------------
#------------------------------------------------------------------ 
# OOP : Objected Oriented Programming
# create a class
"""
# class definition
    class <class-name> :
        methods and properties
# class init by constructor
 obj = <class-name>(parameters...)
"""
class MyClass:
    x = 5

obj = MyClass()
print(obj.x)

class Person:
    # NOTE: __init__(self) is a built-in method in class 
    #       that is called by constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_Person(self):
        print("Hello",self.name, ",", self.age)
"""
# NOTE: The __init__() function is called automatically every time 
#       the class is being used to create a new object.
#
# Note: The self parameter is a reference to the class instance itself,
#       and is used to access variables that belongs to the class.
#
# It does not have to be named self , you can call it whatever
# you like, but it has to be the first parameter of
# any function in the class.
"""

# constructor that calls __init__() function
p1 = Person("Moamen" , 24)
# call properties of an object
print("p1--> name:" ,p1.name , ", age:",p1.age)

# call methods
p1.show_Person()

# modify Object Properties
p1.name = "Mohammed"
p1.age = 55
p1.show_Person()
# Delete Object Properties
del p1.age
# p1.show_Person() # if you try to execute that method it will raise
# AttributeError: 'Person' object has no attribute 'age'

# Delete Objects
del p1
# print(p1) # if you try to execute that method it will raise
# NameError: name 'p1' is not defined

class Student:
    "this class reperesent students"
    
    # class attribute = static member
    std_count = 0
        
    def __init__(self , id=0 , name="" , address=""):
        self.id = id
        self.name = name
        self.address = address
        Student.std_count += 1
        
    def count(self):
        return Student.std_count
  
print(Student.count())

print(Student())
print(Student.count())

s1 = Student(1020,"Moamen" , "Sers")
print(Student.__doc__ , end="\n\n")
print(Student.__name__, end="\n\n")
print(Student.__module__, end="\n\n")
print(Student.__dict__, end="\n\n")
print(Student.__bases__, end="\n\n")

# Class method vs Static Method
# ----------------------------------------------------------
# A class method takes cls as first parameter
# while a static method needs no specific parameters.
# A class method can access or modify class state
# while a static method can’t access or modify it.
# In general, static methods know nothing about class state.
# They are utility type methods that take some parameters
# and work upon those parameters.
# On the other hand class methods must have class as parameter.
# We use @classmethod decorator in python to create a class method
# and we use @staticmethod decorator to create a static method in python.

# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


    
    

    
















