

from basic0 import head
from basic0 import comment
from basic0 import title
from basic0 import qoute_str

import string

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

    print("ord('a') =", ord("a"))
    print("chr('97') =", chr(97))
    
    # substring NOTE: (last index not included)
    s2 = "Moamen soroor"
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

    # string.upper() return a uppercase string
    print('s2.upper() = ' + s2.upper()) # s2.upper() = MOAMEN SOROOR

    # string.lower() return a lowercase string
    print('s2.lower() = ' + s2.lower()) # s2.lower() = moamen soroor

    # string.swapcase() return a swapcase string capital 
    # will be small and vice versa
    print("MoaMen".swapcase())
    # RESULT: 'mOAmEN'

    # string.title() return a string that is first char is capitalized
    print('"moamen soroor here !!".title() = ' + "moamen soroor here !!".title())
    # RESULT: 

    # string.capwords() return a capwords string
    print('string.capwords("moamen soroor here !!") = ' + string.capwords("moamen soroor here !!"))
    # RESULT: 

    # string.replace(string,new_string) return a string with chars
    # replaced with new one
    print('s2.replace("o" , "#") = ' + s2.replace("o" , "#"))
    #RESULT: s2.replace()= M#amen s#r##r

    print("Moamen Soroor".center(40,'#'))
    #RESULT:#############Moamen Soroor##############
    print("Moamen Soroor".center(40,'#'))
    #RESULT:*************Moamen Soroor**************
    print("Moamen Soroor".center(40,'*').center(50,'#'))
    #RESULT:#####*************Moamen Soroor**************#####

    s = "Moamen Soroor"
    lens = len(s)
    print(s.center(3 * lens //2 , '-').center(3 * lens , '*' ))
    #RESULT:**********---Moamen Soroor---**********
    print(s.center(2 * lens , '-').center(3 * lens , '*' ))
    #RESULT:*******------Moamen Soroor-------******

    ## ------------------------ find() method ------------------------------
    ## The find method finds a substring within a larger string.
    ## It returns the leftmost index where the substring is found.
    ## If it is not found, –1 is returned

    print("Moamen Mohammed Gamal Soroor".find("men"))
    # 3
    print("Moamen Mohammed Gamal Soroor".find("Sor"))
    # 22
    print("Moamen Mohammed Gamal Soroor".find("G"))
    # 16

    print("Moamen Mohammed Gamal Soroor".find("Teller"))
    # -1
    # when -1 returns from find function it means that string not found
    subject = '$$$ Get rich now!!! $$$'
    print(subject.find('$$$'))
    # 0
    print(subject.find('$$$', 1)) # Only supplying the start
    # 20
    print(subject.find('!!!'))
    # -1
    print(subject.find('!!!', 0, 16)) # Supplying start and end
    # -1

    # Note: study string methods:
    # rfind, index, rindex, count, startswith, endswith.

    ## ------------------------------ join(sequence) method ----------------------------
    ## A very important string method, join is the inverse of split.
    ## It is used to join the elements of a sequence
    print("\\".join(("C:","user" , "moamen" , "documents")))
    # RESUTL:C:\user\moamen\documents
    print(' - '.join(list(map(lambda s :str(s) ,range(0,10)))))
    # RESULT:0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9

    print(' - '.join(list(map(lambda s :str(s) ,range(0,15)))))
    # RESULT:0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12 - 13 - 14
    ## ------------------------------ splite() method ----------------------------

    print("My Name is Moamen Soroor".split(" ")) # splite by space
    # string.splite(regex or splitting string) return list of splited strings
    print('"Moamen Soroor".split("o")= ' + str("Moamen Soroor".split("o")))
    #RESULT: s2.split("o")= ['M', 'amen s', 'r', '', 'r']

    # Study also :  partition, rpartition, rsplit, splitlines
    #               isalnum, isalpha, isdecimal, isdigit, isidentifier,
    #               islower, isnumeric, isprintable, isspace, istitle, isupper

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

# calling
string_training()
    

