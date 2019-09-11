"""
Documentation here
"""
# ------------------------- modules training -------------------------
# -------------------------------------------------------------------
# import a function from a module
from basic0 import head
from basic0 import comment
from basic0 import title
from basic0 import qoute_str
# normal import
#import cmath
#import datetime
# renaming module in importing the call with new name
import math as m    # call like m.cos(90)
#from random import *
import random


# ------------------------- function training -------------------------
# -------------------------------------------------------------------
# Some Basic Definition
# Parameter:  is variable in the declaration of function.
# Argument: is the actual value of this variable that gets passed to function.

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

my_function()
my_function("Sweden")
my_function("India")
my_function("Brazil")

# NOTE: The default parameters are evaluated at the point of
# function definition in the defining scope.

x = 20
def func1(arg = x):
    "x here will still 20"
    print("func1 arg:",arg)
func1()
x = 25
func1()

# The default value is evaluated only once. This makes a difference 
# when the default is a mutable object such as a list, dictionary, 
# or instances of most classes.

# Immutable default Parameters evaluated once and never changes
def func2(arg = "Moamen"):
    print(arg)
    

# Mutable default Parameters is shared between calls and 
# any call may change it's content
def func3(s1 , arg=[]):
    arg.append(s1)
    return arg

print(func3("Moamen"))
print(func3("Mohammed"))
print(func3("Gamal"))


# To perevent default mutable parameters to 
# be shared you can define functions like below:
def func4(s1 , arg=None):
    if arg == None:
        arg = []
    arg.append(s1)
    return arg

print(func4("Moamen"))
print(func4("Mohammed"))
print(func4("Gamal"))





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

# callable() built-in function to check if variable
# is function or not(callable or not)
x = 10
b = True
print("callable(x)", end=' = ')
print(callable(x))
print("callable(b)", end=' = ')
print(callable(b))
print("callable(pow)", end=' = ')
print(callable(pow))
print("callable(round)", end=' = ')
print(callable(round))

# Documenting function by add a string literal in the first line of it.

def random_1_20():
  "i am a function to return random number from 1 to 20"
  return random.randint(1,20) # random from 1 to 20

print("Enter gen to generate random int or anything else to exit")
while input("[gen or exit]: ") == "gen":
  print(random_1_20())

print("random_1_20.__doc__",end=' = ')
print(random_1_20.__doc__)

# function that doen't return anything, in another word it return None
def func_none_return():
    print("this function doesn't return thing - returns None - ")
    
print("result:",func_none_return())
print("result:",func_none_return())
print("result:",func_none_return())

def print_rand(repeat = 1):
    "print_rand([repeat]) prints a random number from 1 to 20 \
    \with repeation = reapeat default = 1"
    if repeat < 1:
        print("No Repetition as repeat < 1 and =",repeat)
        # note here retrun without any value (None)
        return
    else:
        randlist = []
        for i in range(repeat):
            randlist.append(random.randint(1,20))
        print("random list for repeat {} times = {}".format(repeat,randlist))
        return randlist

print("result of {} is {}".format(-1 ,print_rand(-1)))
print("result of {} is {}".format(0 ,print_rand(0)))
print("result of {} is {}".format(1 ,print_rand(1)))
print("result of {} is {}".format(4 ,print_rand(4)))
print("result of {} is {}".format(6 ,print_rand(6)))

# Collecting parameters

def sum_params(a,b,*c):
    print("input a={}, b={}, *c={}".format(a,b,c))
    result = a + b
    for i in c :
        result += i
    return result


print("sum_params(10,20): ",end="")
print(sum_params(10,20))
print("sum_params(10,20,30): ",end="")
print(sum_params(10,20,30))
print("sum_params(10,20,30,40,50,90): ",end="")
print(sum_params(10,20,30,40,50,90))

# collecting parameters in the middle or the first
# here you should pass parameters after * parameter 
# as a keyword parameter as it can't be accessed
# * Parameter can't be followed by Parameters Except Keyword Parameters

def sum_div_iter(*a,b):
    print("input *a={}, b={}".format(a,b))
    result = sum(a)
    return result//b


print("sum_div_iter(10,b=20): ",end="")
print(sum_div_iter(10,b=20))
print("sum_div_iter(10,20,b=30): ",end="")
print(sum_div_iter(10,20,b=30))
print("sum_div_iter(10,20,30,40,50,60,b=90): ",end="")
print(sum_div_iter(10,20,30,40,50,60,b=90))
# if last value not passed as keyword parameter, Error will be raised
print("sum_div_iter(10,20,30): ",end="")
try:
    print(sum_div_iter(10,20,30))
except TypeError as e:
    print(e)



def sum_div_iter2(*a,b = 2):
    print("input *a={}, b={}".format(a,b))
    result = sum(a)
    return result//b


print("sum_div_iter2(10,b=20): ",end="")
print(sum_div_iter2(10,b=20))
print("sum_div_iter2(10,20,b=30): ",end="")
print(sum_div_iter2(10,20,b=30))
print("sum_div_iter2(10,20,30,40,50,60,b=90): ",end="")
print(sum_div_iter2(10,20,30,40,50,60,b=90))
# if last default parameter is not passed as keyword parameter
# the last value will be in the tuple before and
# last parameter will take default value.
print("sum_div_iter2(10,20,30): ",end="")
print(sum_div_iter2(10,20,30))

# Unpacking Argument Lists
def print_tuple(*t):
    print(t)
    
t = tuple((10,20,30,40))

print_tuple()
print_tuple(10,20,30,40)
print_tuple(*(10,20,30,40))
print_tuple(*t)




def format_string(txt , *args , **kwargs):

    for i in range(0,len(args)):
        holder = "{" + str(i) + "}"
        while True:
            pos = txt.find(holder)
            if pos > -1:
                #txt = txt[:pos] + args[i] + txt[pos+len(holder):]
                txt = txt.replace(holder, str(args[i]))
            else:
                break

    for key , val in kwargs.items():
        holder = "{%s}" % key
        while True:
            pos = txt.find(holder)
            if pos > -1:
                #txt = txt[:pos] + str(val) + txt[pos+len(holder):]
                txt = txt.replace(holder, str(val))
            else:
                break
    return txt

print('format_string("{0} {1} {2}","Moamen" , "Mohammed" , "Gamal")')
print(format_string("{0} {1} {2}","Moamen" , "Mohammed" , "Gamal"))

print('format_string("{0} {1} {two} {three}", "Moamen", "Mohammed", two=2, three=3')
print(format_string("{0} {1} {two} {three}", "Moamen", "Mohammed", two=2, three=3))

# ---------------------------------------------------------------
# passing dictionary or key parameters to functions
def print_params(**d):
    print("print_params: " , end ='')
    print(d)

print_params()
# print_params: {}


try:
    print_params(10)
except Exception as e: print(e)
# TypeError: print_params() takes 0 positional arguments but 1 was given

print_params(a=10)
# print_params: {'a': 10}

print_params(a=10,b=20,c="moamen",d=(True==False))
# print_params: {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}

dic = dict(a=10,b=20,c="moamen",d=(True==False))
print("dic =",dic)
# {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}

try: print_params(dic)
except Exception as e: print(e)
# TypeError: print_params() takes 0 positional arguments but 1 was given

# Unpacking Argument Lists
print_params(**dic)
# print_params: {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}

dic2 = {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}
print("dic2 =",dic2)
# {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}

print_params(**dic2)
# print_params: {'a': 10, 'b': 20, 'c': 'moamen', 'd': False}

# function annotations

def print_str(s1 : str , s2 : str = "is Happy"):
    print(s1, s2)
    
print_str("Moamen" , "is here")
print_str("Moamen")

print_str(123 , "is here")
print_str("Momaen" , 20)
print_str(21 , 20)


def func_anno(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", func_anno.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

func_anno('spam')
func_anno('spam' , "eggs")





# ------------------------- Lambda training -------------------------
# -------------------------------------------------------------------

# Python Lambda
# lambda returns a function
title("Python Lambda training")
func1 = lambda x : x + 10
print("func1 = lambda x : x + 10")
print("func1(10) =",func1(10))

# lambda is a short for
def func1_1(x):
    return x + 10

func5 = lambda a,b : a * b
print("func2 = lambda a,b : a * b")
print("func2(10,20) =",func5(10,20))

func6 = lambda a,b,c: a + b + c
print("func3 = lambda a,b,c: a + b + c")
print("func3(10,20,30) =",func5(10,20,30))

# The power of lambda is better shown when you use them
# as an anonymous function inside another function.

# NOTE: Use lambda functions when an anonymous function
#       is required for a short period of time.


def func7(n):
    return lambda a : a * n

doubler = func7(2)
print("doubler = func(2)")
print("doubler(10) =",doubler(10))
print("doubler(20) =",doubler(20))

tripler = func7(3)
print("tripler = func(3)")
print("tripler(10) =",tripler(10))
print("tripler(20) =",tripler(10))



















