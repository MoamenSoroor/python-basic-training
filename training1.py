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

\xhh        haracter with hex value hh
            print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
            RESULT
            Hello World!
            
Some escape sequences are only recognized in string literals. These are:
Escape      Description
\N{name}    Character named name in the Unicode database

\uxxxx	    Character with 16-bit hex value xxxx. Exactly four hexadecimal digits are required.

\Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx. Exactly eight hexadecimal digits are required.

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

# training on string features and print function:
def basic_training():
    head("basic training")
    # use "" for strings
    print("moamen soroor")
    # use '' for strings
    print('hello, world!')
    # add normally ' to "" string
    print("he said : 'hello, world!' to me")
    # concat strings with + using any string boundary ' " for each one
    print("moamen" + ' ' + "soroor" + ' is here')
    # concat strings with comma , that concat with spaces in between elements
    print("moamen" , "soroor","is here")
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
    # // it rounds down or simply said it remove the decimal part (12.34)-> 12
    # the same operation can be done by int() class and floor in math module
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
    # -2^8 here in python is -256 so sign is not present in power operation
    print("NOTE: -2**8 = " + str(-2**8))
    # to add the sign to the power operation use ()
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
    # some notes about built-in print function
    print(10)
    # addition then convert to string , the same as print(str(10+20))
    print(10 + 20)
    # but you can't directly add string to numbers
    # ERROR: at next line
    # print("string here" + 10)
    print("string here" + str(10))

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
    
    # delete variables x,y,z,w
    del x,y,z,w

#========================= string training =========================
#===================================================================
def string_training():
    # String training
    head("String training")
    s1 = "Hello, World!"
    print("s1 = 'Hello, World!'")
    print("len(s1) = " + str(len(s1)))
    print("s1[0] = " + s1[0])
    print("s1[1] = " + s1[1])
    print("s1[2] = " + s1[2])
    print("s1[3] = " + s1[3])
    print("s1[4] = " + s1[4])
    print("s1[5] = " + s1[5])
    print("s1[6] = " + s1[6])
    print("s1[7] = " + s1[7])
    print("s1[8] = " + s1[8])
    print("s1[9] = " + s1[9])
    print("s1[10] = " + s1[10])
    print("s1[11] = " + s1[11])
    print("s1[12] = " + s1[12])
    print("IndexError: string index out of range for next index")
    print("IndexError: s1[13] = ?")
    print("IndexError: s1[14] = ?")
    
    comment("#Note: if index is negative access from the last char -1,-2,-3,...,-len(s)")
    print("s1[-1] = " + s1[-1])
    print("s1[-2] = " + s1[-2])
    print("s1[-3] = " + s1[-3])
    print("s1[-4] = " + s1[-4])
    print("s1[-5] = " + s1[-5])
    print("s1[-6] = " + s1[-6])
    print("s1[-7] = " + s1[-7])
    print("s1[-8] = " + s1[-8])
    print("s1[-9] = " + s1[-9])
    print("s1[-10] = " + s1[-10])
    print("s1[-11] = " + s1[-11])
    print("s1[-12] = " + s1[-12])
    print("s1[-13] = " + s1[-13])
    print("IndexError: string index out of range for next index")
    print("IndexError: s1[-14] = ?")
    print("IndexError: s1[-15] = ?")
    
    comment("or you access from the last charcter by len function")
    print("s1[(len(s1) - 1) --> 12] = " + s1[len(s1) - 1])
    print("s1[(len(s1) - 2) --> 11] = " + s1[len(s1) - 2])
    print("s1[(len(s1) - 3) --> 10] = " + s1[len(s1) - 3])
    print("s1[(len(s1) - 4) --> 9] = " + s1[len(s1) - 4])
    print("s1[(len(s1) - 5) --> 8] = " + s1[len(s1) - 5])
    print("s1[(len(s1) - 6) --> 7] = " + s1[len(s1) - 6])
    print("s1[(len(s1) - 7) --> 6] = " + s1[len(s1) - 7])
    print("s1[(len(s1) - 8) --> 5] = " + s1[len(s1) - 8])
    print("s1[(len(s1) - 9) --> 4] = " + s1[len(s1) - 9])
    print("s1[(len(s1) - 10) --> 3] = " + s1[len(s1) - 10])
    print("s1[(len(s1) - 11) --> 2] = " + s1[len(s1) - 11])
    print("s1[(len(s1) - 12) --> 1] = " + s1[len(s1) - 12])
    print("s1[(len(s1) - 13) --> 0] = " + s1[len(s1) - 13])

    print("access by len() with negative index:")
    print("s1[(len(s1) - 14) --> -1] = " + s1[len(s1) - 14])
    print("s1[(len(s1) - 15) --> -2] = " + s1[len(s1) - 15])
    print("s1[(len(s1) - 16) --> -3] = " + s1[len(s1) - 16])
    print("s1[(len(s1) - 17) --> -4] = " + s1[len(s1) - 17])
    print("... so on until:")
    print("s1[(len(s1) - 22) --> -10] = " + s1[len(s1) - 23])
    print("s1[(len(s1) - 23) --> -11] = " + s1[len(s1) - 24])
    print("s1[(len(s1) - 25) --> -12] = " + s1[len(s1) - 25])
    print("s1[(len(s1) - 26) --> -13] = " + s1[len(s1) - 26])
    
    print("More negative values is out of range:")
    print("IndexError: string index out of range for next indexes")
    print("IndexError: s1[(len(s1) - 27) --> ?] = ?")
    print("IndexError: s1[(len(s1) - 28) --> ?] = ?")
    print("IndexError: s1[(len(s1) - 29) --> ?] = ?")

    
    # substring NOTE: (last index not included)
    s2 = "Moamen soroor"
    s3 = " Moamen Soroor "
    print('s2[2:5] = ' + s2[2:5]) # s2[2:5] = ame
    print('s2[2:] = ' + s2[2:]) # s2[2:] = amen soroor
    print('s2[:5] = ' + s2[:5]) # s2[:5] = Moame
    print('s2[:] = ' + s2[:])   # a copy of string

    print('s2 = "' + s2 + '"')
    print('s2 = "' + s2 + '"')
    print('len(s2) = ' + str(len(s2))) # len(s2) = 13
    # string.strip() function removes blank spaces at prefix and postfix
    print('"  Moamen Soroor  ".strip() = "' + '  Moamen Soroor  '.strip() + '"')
    #RESULT: "  Moamen Soroor  ".strip() = "Moamen Soroor"

    # string.upper(string) return a uppercase string
    print('s2.upper() = ' + s2.upper()) # s2.upper() = MOAMEN SOROOR

    # string.lower(string) return a lowercase string
    print('s2.lower() = ' + s2.lower()) # s2.lower() = moamen soroor

    # string.replace(string,new_string) return a string with chars
    # replaced with new one
    print('s2.replace("o" , "#") = ' + s2.replace("o" , "#"))
    #RESULT: s2.replace()= M#amen s#r##r

    # string.splite(regex or splitting string) return list of splited strings
    print('s2.split(" ")= ' + str(s2.split(" ")))
    #RESULT: s2.split(" ")= ['Moamen','soroor']
    print('s2.split("o")= ' + str(s2.split("o")))
    #RESULT: s2.split("o")= ['M', 'amen s', 'r', '', 'r']
##--------------------------------------------------------------------------

##    # getting user input
##    print("1- Enter your name:")
##    x = input()
##    print(" Hello, " + x)
##
##    # or you can short this like
##    x = input("2- Enter your name:")
##    print(" your name is " + x)
##
##    # or you can short this like
##    print(" your name is " + input("3- Enter your name:"))
##
##    # get radius from input and claculate circle area
##    print("circle area = " + str(math.pi * (float(input("Enter Radius: "))** 2)))
##--------------------------------------------------------------------------

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
##                          in from the left, and let the rightmost bits fall off
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
    
##--------------------------------------------------------------------------
##  python collections:
##      -List is a collection which is ordered and changeable.
##          Allows duplicate members.
##      -Tuple is a collection which is ordered and unchangeable.
##          Allows duplicate members.
##      -Set is a collection which is unordered and unindexed.
##          No duplicate members.
##      -Dictionary is a collection which is unordered,
##          changeable and indexed.
##          No duplicate members.
##--------------------------------------------------------------------------
##  Features    |   List     Tuple      Set     Dictionary
##--------------------------------------------------------------------------
##  ordered     |   yes      yes        no       no
##--------------------------------------------------------------------------
##  indexed     |   yes      yes        no       yes
##--------------------------------------------------------------------------
##  changeable  |   yes      no         yes      yes
##--------------------------------------------------------------------------
##  duplication |   yes      yes        no       no
##--------------------------------------------------------------------------

# what next is collection training
#========================= list training =========================
#==================================================================
def list_training():
    head("list training")
    list1 = ["apple" , "banana" , "kiwi" , "cherry"]
    print(list1)
    comment("access items with index")
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
    comment("Change item value with index")
    comment("change apple at index 0 to orange")
    list1[0] = "orange"
    print(list1)
    # list1 = ["orange" , "banana" , "kiwi" , "cherry"]

    # change cherry at index 3 to lemon
    comment("change cherry at index 3 to lemon")
    list1[3] = "lemon"
    print("list[3] from cherry to lemon: " + str(list1))
    # list1 = ["orange" , "banana" , "kiwi" , "cherry"]

    comment("loop through list")
    for item in list1:
        print("list1 item: " + item)

    comment("check if item exist")
    if "apple" in list1:
        print("yes, apple exist in list1")
    else:
        print("no, apple not exists in list1")

    comment("get the length of the list")
    print("list1 length = " + str(len(list1)))

    # insert() append() remove() pop() clear()
    # index() reverse() sort() copy() count() extend()
    # del all list, and del item with index
    list1.insert(0 , "lemon")
    print("insert at 0 lemon: " + str(list1))

    list1.append("kiwi")
    print("append kiwi: " + str(list1))
    
    list1.append("banana")
    print("append banana: " + str(list1))

    # it will remove only banana at the index 
    list1.remove("banana")
    print("remove banana: " + str(list1))

    # pop the last index item
    item = list1.pop()
    print("popped item: " + item)
    print("list1: " + str(list1))

    # pop the last item: last index
    item = list1.pop(len(list1) - 1)
    print("popped item[last index]: " + item)
    print("list1: " + str(list1))

    # pop the first item: index of 0
    print("popped item[first index]: " + list1.pop(0))
    print("list1: " + str(list1))

    # pop item[2] third item
    print("popped item[2]: " + list1.pop(2))
    print("list1: " + str(list1))


    # clear all items
    list1.clear()

    # del keyword to delete item with it's index
    # also del used to delete list object from memory
    # NOTE: remove function removes item with it's value,
    #       but del remove with index

    comment("del keyword")
    list1 = [10 , 20 , 30 , 40 , 50]
    print("list1: "+ str(list1))
    # delete item index of 2 = 30
    del list1[2]
    print("list1 after del: "+ str(list1))

    # delete the list object from memory
    del list1
    # initialize empty list
    list1 = []
    # another way to initialize list is to use constructor list(( ))
    list1 = list(("apple" , "banana" , "kiwi" ))
    print("list1= " + str(list1))

    # delete all items from list and keep the list object
    # another way is to use clear()
    del list1[2]
    del list1[1]
    del list1[0]

    # append items
    list1.append("moamen")
    list1.append("mohammed")
    list1.append("gamal")
    list1.append("mohammed")
    list1.append("ahmed")
    list1.append("soroor")
    comment("items of list1 by for in loop")
    for item in list1:
        print(item)

    print("list1= " + str(list1))

    comment("index of an item")
    print("index of " + list1[0] + ": " + str(list1.index("moamen")))
    print("index of " + list1[1] + ": " + str(list1.index("mohammed")))
    print("index of " + list1[2] + ": " + str(list1.index("gamal")))
    print("index of " + list1[4] + ": " + str(list1.index("ahmed")))
    print("index of " + list1[5] + ": " + str(list1.index("soroor")))

    # reverse list
    list1.reverse()
    print("reversed list: " + str(list1))

    # sort list
    list1.sort()
    print("sorted list: " + str(list1))


    # sort list
    list2 = [100 , 50 , 20 , 60 , 40 , 90 , 10]
    print("list to sort: " + str(list2))
    list2.sort()
    print("sorted list: " + str(list2))

    # copy
    comment("copy lists by copy() function")
    list3 = list2.copy()
    print("list2: " + str(list2))
    print("list3: " + str(list3))

    comment("copy by slicing")
    print("slice list3[:]=",list3[:])
    

    # Extend() function
    comment("Extend() function")
    list3.extend([110 , 120 , 130])
    print("extension: " + str([110 , 120 , 130]))
    print("extended list3: " + str(list3))

    list4 = [115 , 120 , 125]
    print("extension: " + str(list4))
    list3.extend(list4)
    print("extended list3: " + str(list3))

    # count() function
    comment("count() function")
    print("count 120 in list3 : " + str(list3.count(120)))
    # delete all lists
    del list1
    del list2
    del list3
    del list4
    print("list1, list2, list3, list4 has deleted successfully")
    # slicing
    comment("slicing lists")
    a = [1,2,3,4,5,6,7,8,9,10]
    print("list a =",a)
    print("list len(a) =",len(a))
    print("list max(a) =",max(a))
    print("list min(a) =",min(a))
    print("list sum(a) =",sum(a))
    print("copy a[:]=",a[:])
    print("slice a[0:5]=",a[0:5])

list_training()  
   

#========================= tuple training =========================
#==================================================================
def tuple_training():
    head("tuple training")
    t1 = ("moamen" , "mohammed" , "gamal" , "soroor")
    print("tuple t1 =",t1)
    print("tuple t1 type =",type(t1))
    print("tuple t1 length =",len(t1))
    
#========================= set training =========================
#==================================================================
def set_training():
    head("set training")
    # NOTE: sets doesn't allow duplication of items,
    #           also it is unordered and unindexed
    # set functions is:
    #   add()       --> add new item
    #   update()    --> add items to set
    #   union()     --> return new set with items of sets in input
    #                       ex. s3 = s1.union(s2, s3)
    #   pop()       --> poped item is unknown as order of set is ambiguous
    #   remove()    --> remove item by it's value ex. s1.remove("moamen")
    #   discard()   --> the same like remove, but if the item is not exists,
    #                   it doesn't raise an error,
    #                   opposite to remove it raise an error
    #   clear()     --> remove all items from the set
    #   copy()      --> return a copy of all items ex. s2 = s2.copy()
    #   isdisjoint()        --> retrun true if there is no joint between lists
    #   issubset()          --> return true if set is sub of another set
    #   issuperset()        --> return true if the set contains the other set
    #   intersection()      --> Return a set that contains the items that
    #                           exist in both set x, and set y
    #   intersection_update()   --> Remove the items that is not present
    #                               in both x, and set y
    #   difference()            --> return set with items in s1 that not exists in s2
    #   difference_update()     --> remove items in s1 that exists in s2
    #   symmetric_difference()  --> return set with items of both sets except
    #                               items that exists in both sets
    #   symmetric_difference_update()   --> update set with both sets items
    #                                       except items exists in both sets
    print("set training")



#========================= dictionary training =========================
#==================================================================
def dictionary_training():
    head("dictionary training")
    dic = {
	"fname" : "moamen",
	"lname" : "soroor",
	"age" : 24,
	"hobby" : "gaming"
	}
    print(dic)

    # dictionary access
    comment("access dictionary with key")
    print("dic['fname'] = " + str(dic["fname"]))
    print("dic['lname'] = " + str(dic["lname"]))
    print("dic['age'] = " + str(dic["age"]))
    print("dic['hobby'] = " + str(dic["hobby"]))

    print("using get function: ")
    print("dic.get('fname') = ", dic.get("fname"))
    print("dic.get('lname') = ", dic.get("lname"))
    print("dic.get('age') = ", dic.get("age"))
    print("dic.get('hobby') = ", dic.get("hobby"))

    # change value for specific key
    comment("change value for specific key")
    dic["age"] = 25
    dic["hobby"] = "football"
    print("dic list:" , dic)

    # first, lets try some functions
    comment("functions keys() , values() , and items()")
    # NOTE: values() return all values , all keys() returns keys ,
    #   items() returns pair of key , and value
    keys = dic.keys()
    values = dic.values()
    items = dic.items()
    print("dic.keys():", keys)
    print("dic.values():", values)
    print("dic.items():", items)
    # types
    print("type(dic.keys()):", type(keys))
    print("type(dic.values()):", type(values))
    print("type(dic.items()):", type(items))

    # loop through dicionary items

    comment("loop through dicionary items")

    comment("for..in to get keys directly: ")
    for k in dic:
        print("k:",k,"v:",dic[k]) # or print("k:",k,"v:",dic.get(k))

    comment("for..in to get keys by keys(): ")
    for k in dic.keys():
        print("k:",k,"v:",dic[k]) # or print("k:",k,"v:",dic.get(k))

    comment("for..in to get values() with values(): ")
    for v in dic.values():
        print("v:",v)

    comment("for..in to get k , v with items(): ")
    for k , v in dic.items():
        print("k:",k,"v:",v)

    comment("Adding new Item to dictionary dic")

    dic["job"] = "engineer"
    dic["country"] = "Egypt"
    dic["potal_code"] = 18456

    print("dic:" , dic)

    comment("Removing Items from dictionary dic")
    comment("last item removing by - using popitem() - should return postal_code k,v")
    print("poped item:",dic.popitem())
    print("dic:" , dic)

    comment("pop an item - using pop() - with it's key from dictionary dic")
    print("poped item:", dic.pop("country"))
    print("dic:" , dic)

    comment("remove item - using del - with it's key from dictionary dic")

    del dic["job"]
    print("deleted item key: job ")
    print("dic:" , dic)

    comment("delete the dictionary form memory with it's items")
    del dic
    # ERROR: print(dic)
    # UnboundLocalError: local variable 'dic' referenced before assignment

    #initialize with constructor dict()
    comment("allocate dictionary dic with constructor dict()")
    dic = dict(fname = "moamen", lname = "soroor" ,
               age = 24 , hobby = "gaming")
    print("dic: " , dic)

    # functions clear() copy() fromkeys() setdefault()
    # copy then clear()
    comment("copy() function")
    dic2 = dic.copy()
    comment("clear() function")
    dic.clear()
    print("cleared dic:",dic)

    comment("add items to dic again without new memory allocation")
    dic["fname"] = "moamen"
    dic["lname"] = "soroor"
    dic["age"] = 24
    print("dic: " , dic)
    del dic , dic2
    print("delete dictionaries: dic and dic2")
    # print("dic: " , dic2)
    # print("dic1: " , dic)

#========================= Control flow training =========================
#=========================================================================
# if elif else
# while
# for in
def control_flow_training():
    head("control flow training")
    # -------------------------------- if statement -----------------------------
    title("if-elif-else statements")
    a = 200
    b = 33
    print("a =",a)
    print("b =",b)
    if b > a:
      print("b is greater than a")
    elif a == b:
      print("a and b are equal")
    else:
      print("a is greater than b")

    comment("Short hand if or one line if")
    if a < b : print("a is greater than b")

    comment("Short hand if else or one line if else")
    print("a is greater than b") if a > b else print("b is greater than a")
    a = b = 35
    b = 40
    x = 10 if a > b else 20 if a == b else 15
    print("x =" , x)
    # -------------------------------- while loop -----------------------------
    title("while loop")
    s1 = "moamen soroor"
    i = 0;
    while i < len(s1):
        print("s1[" + str(i) + "]= " + '"' + s1[i] + '"')
        i += 1

    # break statement : break at index 7 = s
    comment("breake statement")
    i = 0;
    while i < len(s1):
        if i > 7: break
        print("s1[" + str(i) + "]= " + '"' + s1[i] + '"')
        i += 1
        

    # continue statement : skip space at index = 6
    comment("continue statement")
    i = 0;
    while i < len(s1):
        if i == 6 :
            i += 1
            continue
        print("s1[" + str(i) + "]= " + '"' + s1[i] + '"')
        i += 1

    # -------------------------------- for loop -----------------------------
    title("for loop")
    # access list using in operator
    comment("for in loop")
    fruits = ["apple", "banana", "cherry"]
    print("fruits =",fruits)
    comment("print list with for-in")
    for x in fruits: 
      print(x)

    # string treated as a sequence of charcters (immutable list)
    comment("print character of immutable string")
    for x in "banana":
      print(x)

    comment("for in with break statement at banana")
    for x in fruits:
      print(x) 
      if x == "banana":
        break

    for x in fruits:
      if x == "banana":
        break
      print(x)

    comment("for in with continue statement at banana")
    for x in fruits:
      if x == "banana":
        continue
      print(x)
    comment("for-in with range function that generate list")
    # Note that range(6) makes list starts from 0 ends with 5 with step 1
    comment("range(6) start = 0, end = 5, and step = 1")
    for x in range(6):
      print(x)

    # Note that range(2,6) makes list starts from 2 ends with 5 with step 1
    comment("range(2,6) start = 2, end = 5, and step = 1")
    for x in range(2, 6):
      print(x)

    # Note that range(2,30,3) makes list starts from 2 ends with 29 with step 3
    comment("range(2,30,3) start = 2, end = 29, and step = 3")
    for x in range(2, 30, 3):
      print(x)

    comment("for loop prints from 1 to 6 then, else-statement executed")
    for x in range(6):
      print(x)
    else:
      print("Finally finished!")


    # nested loops
    comment("nested loops")
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    print("adj =",adj)
    print("fruits =",fruits)
    for x in adj:
      for y in fruits:
        print(x, y)


# ---------------------------- function calls -------------------------    
#basic_training()
#string_training()
#operators_training()
#list_training()
#tuple_training()
#set_training()
#dictionary_training()
#control_flow_training()
