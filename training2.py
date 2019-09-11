"""
Documentation here
"""
# ------------------------- modules training -------------------------
# -------------------------------------------------------------------
# import a function from a module
from chapter1 import comment 
from chapter1 import head 
from chapter1 import title
# normal import
import cmath
import datetime
# renaming module in importing the call with new name
import math as m    # call like m.cos(90)


# ------------------------- function training -------------------------
# ------------------------------------------------------------------- 
# define a function
def my_function():
  print("Hello from a function")

# call function
my_function()


# Parameters
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Return Value with default parameter b = 2
def pow(a , b = 2):
    return a ** b

print("pow(2) =",pow(2)) # return will be 2^2
print("pow(2,3) =",pow(2,3)) # return will be 2^3

# ------------------------- Lambda training -------------------------
# ------------------------------------------------------------------- 

# Python Lambda
# lambda returns a function
func1 = lambda x : x + 10
print("func1 = lambda x : x + 10")
print("func1(10) =",func1(10))

# lambda is a short for
def func1_1(x):
    return x + 10

func2 = lambda a,b : a * b
print("func2 = lambda a,b : a * b")
print("func2(10,20) =",func2(10,20))

func3 = lambda a,b,c: a + b + c
print("func3 = lambda a,b,c: a + b + c")
print("func3(10,20,30) =",func3(10,20,30))

# The power of lambda is better shown when you use them
# as an anonymous function inside another function.

# NOTE: Use lambda functions when an anonymous function
#       is required for a short period of time.


def func4(n):
    return lambda a : a * n

doubler = func4(2)
print("doubler = func(2)")
print("doubler(10) =",doubler(10))
print("doubler(20) =",doubler(20))

tripler = func4(3)
print("tripler = func(3)")
print("tripler(10) =",tripler(10))
print("tripler(20) =",tripler(10))

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

# ------------------------- Iterator training -------------------------
# ------------------------------------------------------------------- 
"""
##  Python Iterators
## An iterator is an object that contains a countable number of values.
## 
## An iterator is an object that can be iterated upon, meaning that you
## can traverse through all the values.
## 
## Technically, in Python, an iterator is an object which implements
## the iterator protocol, which consist of the
## methods __iter__() and __next__().
##
## Iterator vs Iterable
## Lists, tuples, dictionaries, and sets are all iterable objects.
## 
## They are iterable containers which you can get an iterator from
## All these objects have a iter() method which is used to
## get an iterator
"""

list1 = list(range(10,100,10))
print("list1:",list1)


# interate over all list members
my_iter = iter(list1)
for i in range(len(list1)):
    print("next(my_iter) =",next(my_iter))

# create an Iterator  / custom iterator
class IntegerSequence1:
    
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
comment("integer sequence by iter")
int_seq = IntegerSequence1()
my_iter = iter(int_seq)

print("next(my_iter) =",next(my_iter))
print("next(my_iter) =",next(my_iter))
print("next(my_iter) =",next(my_iter))
print("next(my_iter) =",next(my_iter))
print("next(my_iter) =",next(my_iter))
print("next(my_iter) =",next(my_iter))

# NOTE: for loop actually creates an iterator object
#       and executes the next() method for each iterator

class IntegerSequence2:
    
    
    def __iter__(self):
        self.end = 10
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= self.end:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
comment("custom iterator in for in")
int_seq = IntegerSequence2()

for x in int_seq:
    print("x =",x)
    
comment("custom iterator in normal iteration")
int_seq = IntegerSequence2()
my_iter = iter(int_seq)

print("next(my_iter)--> 1 =",next(my_iter))
print("next(my_iter)--> 2 =",next(my_iter))
print("next(my_iter)--> 3 =",next(my_iter))
print("next(my_iter)--> 4 =",next(my_iter))
print("next(my_iter)--> 5 =",next(my_iter))
print("next(my_iter)--> 6 =",next(my_iter))
print("next(my_iter)--> 7 =",next(my_iter))
print("next(my_iter)--> 8 =",next(my_iter))
print("next(my_iter)--> 9 =",next(my_iter))
print("next(my_iter)--> 10 =",next(my_iter))

# StopIteration will be raised if next 2 functions executed
# print("next(my_iter)--> 11 =",next(my_iter))
# print("next(my_iter)--> 12 =",next(my_iter))


# ------------------------- Exceptions training -------------------------
# -----------------------------------------------------------------------
def div(a,b):
  try:
    return a/b
  except ZeroDivisionError:
    print("ZeroDivisionError: zero div occurred")
  except ValueError:
    print("ValueError: value error accurred")
  except:
    print("Unknown Error , an error occurred")
  else:
    print("Safe Execution: else block generated")
  finally:
    print("finally block generated")

#print("div(10,2) =", div(10,2))
#print("div(10,0) =", div(10,0))
print("div(10,'moamen') =", div(10,"moamen"))



















