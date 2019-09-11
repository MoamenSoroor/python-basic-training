r"""
this is documentation string
it is multiline head
-----------------------------------------------------------------
 Escape sequences
-----------------------------------------------------------------
\newline    Backslash and newline ignored
\\	    Backslash (\)
\'	    Single quote (')
\"	    Double quote (")
\a	    ASCII Bell (BEL)
\b	    ASCII Backspace (BS)
\f	    ASCII Formfeed (FF)
\n	    ASCII Linefeed (LF)
\r	    ASCII Carriage Return (CR)
\t	    ASCII Horizontal Tab (TAB)
\v	    ASCII Vertical Tab (VT)
\ooo	    Character with octal value ooo
            print("\110\145\154\154\157\40\127\157\162\154\144\41")
            RESULT
            Hello World!

\xhh        character with hex value hh
            print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
            RESULT
            Hello World!
            
Some escape sequences are only recognized in string literals. These are:
Escape      Description
----------  ---------------------------------------------------------------
\N{name}    Character named name in the Unicode database

\uxxxx	    Character with 16-bit hex value xxxx. Exactly four hexadecimal
            digits are required.

\Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx. 
            Exactly eight hexadecimal digits are required.

"""

# imports...
import math
import cmath

# head(string) is to print big titles for each important functions
def head(s):
    print("\n####HEAD:=============== " + s + " ===============")
    print("         =============== " + ('=' * len(s)) + " ===============")

# title of each section in code
def title(s):
    print("\n###TITLE:=========== " + s + " ===========###")

# comment(string) is to print small titles in interpriter
def comment(s):
    print("\n##COMMENT:===== " + s + " =====##")

def qoute_str(s):
    return '"' + s + '"'

def sep(length = 40 , chars = "-"):
    print(chars * length)

# training on string features and print function:
def basic_training():
    head("basic training")
    # use "" for strings
    print("moamen soroor")
    # use '' for strings
    print('hello, world!')
    # add normally ' to "" string
    print("he said : 'hello, world!' to me")
    # concat strings with + operator using any string boundary ' " 
    # for each one
    print("moamen" + ' ' + "soroor" + ' is here')
    
    # concat strings with comma , that concat with spaces in between elements
    print("moamen" , "soroor","is here")

    # concat strings using sep='-'
    print("moamen" , "soroor","is here",sep="-")

    # concat strings using sep='-' and end="$"
    print("moamen" , "soroor","is here",sep="-" , end = "$")
    print("rest of line")
    
    # ---- some math ----
    title("Some math training")
    # multiplication and convert to string
    print("12*10 = " + str(12*10))
    # summation and ...
    print("12 + 11 - 1 = " + str(12 + 11 - 1))
    # division
    print("12/4 = " + str(12/4))
    print("23.1/5.23 = " + str(23.1/5.23))
    # integer division or floor division
    # // it rounds down or simply said it removes the decimal part 
    # (12.34)-> 12 , while the same operation can be done by 
    # int() class and floor in math modules
    comment("round down or floor with // operator")
    print("10//3 = " + str(10//3))      # should be 3
    print("-10//3 = " + str(-10//3))    # should be -4
    print("10//-3 = " + str(10//-3))    # should be -4
    print("-10//-3 = " + str(-10//-3))  # should be 3
    # by int
    print("int(10/3) = " + str(int(10/3)))
    print("int(-10/3) = " + str(int(-10/3)))
    print("int(10/-3) = " + str(int(10/-3)))
    print("int(-10/-3) = " + str(int(-10/-3)))
    # by math.floor()
    comment("round down by math.floor() function")
    print("math.floor(10/3) = " + str(math.floor(10/3)))
    print("math.floor(-10/3) = " + str(math.floor(-10/3)))
    print("math.floor(10/-3) = " + str(math.floor(10/-3)))
    print("math.floor(-10/-3) = " + str(math.floor(-10/-3)))
    print("math.floor(3.6) = " + str(math.floor(3.6)))
    print("math.floor(3.5) = " + str(math.floor(3.5)))
    print("math.floor(3.4) = " + str(math.floor(3.4)))
    print("math.floor(-3.6) = " + str(math.floor(-3.6)))
    print("math.floor(-3.5) = " + str(math.floor(-3.5)))
    print("math.floor(-3.4) = " + str(math.floor(-3.4)))

    # round up by ceil function in math module
    # by math.ceil()
    comment("round up by math.ceil() function")
    print("math.ceil(10/3) = " + str(math.ceil(10/3)))
    print("math.ceil(-10/3) = " + str(math.ceil(-10/3)))
    print("math.ceil(10/-3) = " + str(math.ceil(10/-3)))
    print("math.ceil(-10/-3) = " + str(math.ceil(-10/-3)))
    print("math.ceil(3.6) = " + str(math.ceil(3.6)))
    print("math.ceil(3.5) = " + str(math.ceil(3.5)))
    print("math.ceil(3.4) = " + str(math.ceil(3.4)))
    print("math.ceil(-3.6) = " + str(math.ceil(-3.6)))
    print("math.ceil(-3.5) = " + str(math.ceil(-3.5)))
    print("math.ceil(-3.4) = " + str(math.ceil(-3.4)))

    # built-in round() function: it rounds to the nearest integer value
    # if fraction part is equal or more than 0.5 , it rounds up
    # else it rounds down
    comment("round to the nearest integer by round() function")
    print("round(3.6) = " + str(round(3.6)))
    print("round(3.5) = " + str(round(3.5)))
    print("round(3.4) = " + str(round(3.4)))
    print("round(-3.6) = " + str(round(-3.6)))
    print("round(-3.5) = " + str(round(-3.5)))
    print("round(-3.4) = " + str(round(-3.4)))
    # power
    comment("Power operator ** ex. 2 ** 3 = 8")
    print("2.2**8.3 = " + str(2.2**8.3))
    print("2**8 = " + str(2**8))
    # -2^8 here in python is -256 so minus sign is 
    # not presented in power operation.
    print("NOTE: -2**8 = " + str(-2**8))
    # to add the sign to the power operation use parentheses()
    print("NOTE: (-2)**8 = " + str((-2)**8))

    # more tests
    print("2**-8 = " + str(2**-8))
    print("2**(-8) = " + str(2**(-8)))
    print("(-2)**-8 = " + str((-2)**-8))
    print("(-2)**(-8) = " + str((-2)**(-8)))

    # pow function to calculate power
    comment("Power function pow(a,b)")
    print("pow(2,8) = " + str(pow(2,8)))
    print("pow(-2,8) = " + str(pow(-2,8)))
    print("pow(2,-8) = " + str(pow(2,-8)))
    print("pow(-2,-8) = " + str(pow(-2,-8)))

    # modulus operator %
    comment("modulus operator %")
    print("20%3 = " + str(20%3))
    print("10%2 = " + str(10%2))
    print("19%3 = " + str(19%3))
    # modulus with negative values
    # n is numerator , d is denominator , r is result
    # +n % +d => +r % +d => r
    # -n % -d => -r % -d => -r
    # -n % +d => -r % +d => -r + d
    # +n % -d => +r % -d => r - d

    # 10%3 => (9+1)%3 => 1%3 => 1
    print("NOTE: 10%3 = " + str(10%3))
    # -10%3 => (-9-1)%3 => -1%3 => -1 + 3 = 2
    print("NOTE: -10%3 = " + str(-10%3))
    # 10%-3 => (9+1)%-3 => 1%-3 => 1 - 3 = -2
    print("NOTE: 10%-3 = " + str(10%-3))
    # -10%-3 => (-9-1)%-3 => -1%-3 => -1
    print("NOTE: -10%-3 = " + str(-10%-3))

    # some built-in functions
    
    # dir() function
    print("dir(math) = ",dir(math))
    # print all functions associate with a specefic type
    a = 10
    b = 20.45
    c = "Hello"
    d = 20 -1j
    print(dir(a))
    print(dir(b))
    print(dir(c))
    print(dir(d))
    # help() function
    print(help(a))
    print(help(b))
    print(help(c))
    print(help(d))
    
    #  type() function
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    
    # id() function
    x = 10
    y = 20
    z = 30.2
    print("id(x) =",id(x))
    print("id(y) =",id(y))
    print("id(z) =",id(z))
    
    # oct and bin and hex function
    print(hex(123))
    print(oct(123))
    print(bin(123))
    
    # ord and chr
    print(ord('a'))
    print(ord('b'))
    print(ord('A'))
    print(ord('B'))
    print(chr(97))
    print(chr(98))
    print(chr(65))
    print(chr(66))
    
    
    
    
    
    
    
    # some notes about built-in print function
    print(10)
    # addition then convert to string , the same as print(str(10+20))
    print(10 + 20)
    # but you can't directly add string to numbers
    # ERROR: at next line
    # print("string here" + 10)
    print("string here" + str(10))
    
    # print end and sep parameters
    # default values is end="\n" sep=" "
    print("this text is",end='')
    print(" ended here.")
    
    print("I" , "am" , "Moamen" , "Soroor" , sep=" ")
    print("this" , "text" , "is" , sep = " " , end ="" )
    print(" ended here.")
    
    print("Hello world" , end = "##")

    # variables
    # integers
    comment("Variables")
    x1 = 10
    x2 = x1 * 2
    print(x2)
    print(x1*2 + 1)
    # floats
    f1 = 3.14
    # strings
    s1 = "moamen"
    # complex numbers associate with cmath module
    c1 = 2 + 3j
    c2 = -2 + 3j
    c3 = 2 - 3j
    c4 = -2 - 3j
    c5 = -3j
    c6 = -4 + 0j
    print("c1 =",c1)
    print("c2 =",c2)
    print("c3 =",c3)
    print("c4 =",c4)
    print("c5 =",c5)
    print("c6 =",c6)
    
    # types of variables
    x1 = 100
    x2 = -19292123123
    x3 = 323e-29
    x4 = 323e29
    print("type(x1 = 100) = " + str(type(x1)))
    print("type(x2 = -19292123123) = " + str(type(x2)))
    print("type(x3 = 323e-29) = " + str(type(x3)))
    print("type(x4 = 323e29) = " + str(type(x4)))

    print("type(f1 = 3.14) = " + str(type(f1)))

    print("type(c1 = -2 + 3j) = " + str(type(c1)))
    print("type(c2 = -2 + 3j) = " + str(type(c2)))

    # Types in python
    # int float complex str object
    
    # casting int() float() string()
    # integers
    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3

    # floats
    x = float(1)     # x will be 1.0
    y = float(2.8)   # y will be 2.8
    z = float("3")   # z will be 3.0
    w = float("4.2") # w will be 4.2

    # strings
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0'
    
    x1 = complex(10)
    x2 = complex(10j)
    x3 = complex(real=10, imag=30)
    y = complex(10,20)
    z = complex(-10,20)
    w = complex(-10,-20)
    print((x1,x2,x3,y,z,w))
    
    # delete variables x,y,z,w
    del x1,x2,x3,y,z,w

##--------------------------------------------------------------------------  
##  Python Operators
##    1- Arithmetic Operators: + - / // * ** %
##    2- Assignment Operators: = += -= /= //= *= **= %= &= |= ^= >>= <<=
##    3- Comparison Operatoes: == != < <= > >=
##    4- Logical Operators:
##         and
##         or
##         not
##    5- Identity Operators:       is      is not
##         -Identity operators are used to compare the objects,
##         not if they are equal, but if they are actually the same object,
##         with the same memory location
##
##         is
##         is not
##    6- Membership Operators:     in      not in
##         -Membership operators are used to test if a sequence
##         is presented in an object:
##
##         in - Returns True if a sequence with the specified value is
##             present in the object not in - Returns True if a sequence
##             with the specified value is not present in the object
##    7- Bitwise Operators: Bitwise operators are used to compare
##             (binary) numbers:
##              & 	AND	Sets each bit to 1 if both bits are 1
##              |	OR	Sets each bit to 1 if one of two bits is 1
##              ^	XOR	Sets each bit to 1 if only one of two bits is 1
##              ~ 	NOT	Inverts all the bits
##              <<	Zero fill left shift
##                          Shift left by pushing zeros in from
##                          the right and let the leftmost bits fall off
##              >>	Signed right shift
##                          Shift right by pushing copies of the leftmost bit
##                          in from the left, and let the rightmost bits fall
##                          off
##--------------------------------------------------------------------------

def operators_training():
    head("operators training")
    # note that we discuss Arithmetic operators before.
    #start from assignment operators
    title("Assignment Operator")
    a = 10      # 10
    print("a -->",a)
    a += 10     # 20
    print("a += 10 -->",a)
    a -= 10     # 10
    print("a -= 10 -->",a)
    a *= 10     # 100
    print("a *= 10 -->",a)
    a /= 10     # 10
    print("a /= 10 -->",a)
    a //= 3     # 3
    print("a //= 3 -->",a)
    a **= 3     # 27
    print("a **= 3 -->",a)
    a %= 10     # 7
    print("a %= 10 -->",a)

    # rest of assignment operators are &= |= ^= <<= >>=

    # comparison and logical operators
    title("comparison operator")
    a = 10
    b = 20
    c = 10
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    print("a < b -->",a < b)
    print("a <= b -->",a <= b)
    print("a > b -->",a > b)
    print("a >= b -->",a >= b)
    print("a == b -->",a == b)
    print("a != b -->",a != b)
    print("a == c -->",a == c)
    print("a != c -->",a != c)
    
    print("a > b > c -->",a > b > c)
    print("a >= b >= c -->",a >= b >= c)
    print("a < b < c -->",a < b < c)
    print("a <= b <= c -->",a <= b <= c)
    
    print("a == b == c -->",a == b == c)
    print("a == b != c -->",a == b != c)
    print("a != b == c -->",a != b == c)
    print("a != b != c -->",a != b != c)

    print("a < b == c -->",a < b == c)
    print("a < b != c -->",a < b != c)
    print("a > b == c -->",a > b == c)
    print("a > b != c -->",a > b != c)
    
    title("Logical Operator:  and or not")
    print("a > b and b > c -->" , a > b and b > c )
    print("a < b and b < c -->" , a < b and b < c )
    print("not(a == b) and a == c -->" , not(a == b) and a == c )
    print("a < b or b < c  and not(c == 10) -->" , a < b or b < c  and not(c == 10))
    print("(True and False) or (True and(not (True or False) and True))= ",(True and False) or (True and(not (True or False) and True)))

    title("Identity operators: is , is not")
    print("related to oop")
    title("membership operator: in , not in")
    title("related to collections or data structures")
    title("Bitwise operators: & | ^ ~ << >>")
    ## ...
    
# calling basic_training() function
# basic_training()
# call operator_training() function
# operators_training()
