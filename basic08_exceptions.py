# ------------------------- Exception Handling training -----------------
# -----------------------------------------------------------------------
def div(a,b):
    try:
        return a/b
    except (ZeroDivisionError, ArithmeticError):
        print("ZeroDivisionError: zero div occurred")
    except ValueError as ve:
        print("ValueError: value error accurred")
        print(ve)
    except TypeError:
        # move the TypeError exception to up level by only raise keyword
        raise
    except:
        print("Unknown Error , an error occurred")
    else:
        print("Safe Execution: else block generated")
    finally:
        print("finally block generated")

#print("div(10,2) =", div(10,2))
#print("div(10,0) =", div(10,0))
print("div(10,'moamen') =", div(10,"moamen"))

# Catching more than Exceptions in one block
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus ...')

# Catching the Object
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError) as e:
    print(e)

# try again mechanism
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
    except:
        print('Invalid input. Please try again.')
    else:
        break

# try again mechanism 2
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
    except Exception as ex:
        print('Invalid input: {}'.format(ex))
        print("Please try again")
    else:
        break


# Custom Exceptions
class CustomException(Exception): pass


# The raise Statement
try:
    print("try Block")
    raise Exception("Exception happened!!")
except:
    raise Exception
    raise ArithmeticError
    raise AttributeError
    raise OSError
    raise IndexError
    raise KeyError
    raise NameError
    raise SyntaxError
    raise TypeError
    raise ValueError
    raise ZeroDivisionError



