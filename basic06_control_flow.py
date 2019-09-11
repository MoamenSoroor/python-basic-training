from basic0 import head
from basic0 import comment
from basic0 import title
#from basic0 import qoute_str

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

    # List Comprehension or named Slightly Loopy
    
    print([x for x in range(10)])
    
    # power of 2 list
    print([2 ** x for x in range(10)])
    
    print([x * x for x in range(10)])
    
    print([x for x in range(10) if x % 2 == 0])
    print([x for x in range(10) if x % 2 == 1])
    
    print([ x + y for x in range(4) for y in range(4)])
    
    # code equivalent
    alist = []
    for x in range(4):
        for y in range(4):
            alist.append(x + y)
    
    print(alist)
    
    
    print([ x + y for x in range(4) if x > 2 for y in range(4)])
    
    # code equivalent
    alist = []
    for x in range(4):
        if x > 2:
            for y in range(4):
                alist.append(x + y)
    
    print(alist)
    
    
    
    print([a*a for a in range(10,100,5)])
    print([(x, y) for x in range(3) for y in range(3)])
    

    # map function
    comment("map function")
    # using map function to make a list of evens ** 2
    print("list(map(lambda a: a * a , range(0,20,2)))")
    print(list(map(lambda a: a * a , range(0,20,2))))
    
    print(list(map(lambda a, b : a * b , range(0,20,2) , range(1,21,2))))
    
    
    # zip function
    # zip(*iterables) returns sequence
    title("zip function")
    print(list(zip([1,2,3,4],[11,12,13,14])))
    print(tuple(zip([1,2,3,4],[11,12,13,14])))
    l1 = ["Moamen" , "Mohammed" , "Gamal" , "Soroor"]
    l2 = ["fname" , "mname" , "mname2" , "lname"]
    print("l1 =",l1)
    print("l2 =",l2)
    print("list(zip(l2,l1)) =",list(zip(l2,l1)))
    # zip() function , if two sequences is not equal in length,
    # it stops at the smallest length
    print("list(zip(range(0,10),range(100,100000))) =" ,
          list(zip(range(0,10),range(100,100000))))
    
    # enumerate() function
    # enumerate(iterable, start=0)
    title("enumerate function")
    print(list(enumerate([10,20,30] , 1)))
    print(list(enumerate([10,20,30,40] , start=1)))
    print(list(enumerate(["Moamen" , "Mohammed" , "Gamal"] , start=3)))
    
    l1 = ["Moamen" , "Mohammed" , "Gamal" , "Soroor"]
    for i , value in enumerate(l1,10):
        print(i , value)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
control_flow_training()
 
