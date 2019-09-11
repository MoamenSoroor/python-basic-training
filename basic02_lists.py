
from basic0 import head
from basic0 import comment
from basic0 import title
from copy import deepcopy
#from basic0 import qoute_str

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
#========================= list training ==========================
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

    # make a list by reversed() and [::step]
    comment("make a list by reversed() and [::step]")
    
    list1 = list(reversed([10,20,30,40]))
    print("list(reversed([10,20,30,40]) -->",list1)
    
    print("##### another way to reverse")
    list1 = list([10,20,30,40][::-1])
    print("list([10,20,30,40][::-1]) -->",list1)

    # Sorting lists by sort function
    title("Sorting lists")
    list2 = [100 , 50 , 20 , 60 , 40 , 90 , 10]
    print("list to sort: " + str(list2))
    
    list2.sort()
    print("sorted list: " + str(list2))

    comment("Sorting with reverse parameter")
    list2 = [100 , 50 , 20 , 60 , 40 , 90 , 10]
    print("list to sort: " + str(list2))
    list2.sort(reverse=True)
    print("sorted in reverse=True list: " + str(list2))
    
    
    
    

    # advanced Sorting
    ####### not implemented now ############
    comment("Advance Sorting with key and reverse attributes")
    print("####### not implemented now ############")

    
    # copy()
    comment("copy lists by copy() function")
    list3 = list2.copy()
    print("list2: " + str(list2))
    print("list3: " + str(list3))

    comment("copy by slicing")
    print("slice list3[:]=",list3[:])
    

    # extend() function
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
    comment("list1, list2, list3, list4 has deleted successfully")
    
    a = list(range(10,110,10))
    # a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("list a =",a)
    print("list len(a) =",len(a))
    print("list max(a) =",max(a))
    print("list min(a) =",min(a))
    print("list sum(a) =",sum(a))
    print("copy a[:]=",a[:])
    
    # indexing and negative indexing
    title("indexing and negative indexing")
    comment("positive indexing")
    for i in range(0,10):
        print("a[",i,"] =",a[i])
    comment("negative indexing")
    for i in range(0,10):
        print("a[",i-len(a),"] =",a[i-len(a)])
    
    # slicing
    # SYNTAX: list_name[start_index : end_index]
    # NOTE: end index is not included, 0:3-->0,1,2
    # NOTE: if end_index is for last item then:
    #       end_index = len(list_name)
    # list_name[-start_index : -end_index]
    title("slicing from a list")
    comment("slice a[0:10] = a[0:] = a[:10] = a[:] = a.copy()")
    print("slice a[0:10]=",a[0:10])
    print("slice a[:10]=",a[:10])
    print("slice a[0:]=",a[0:])
    print("slice a[:]=",a[:])
    print("slice a[0:len(a)]=",a[0:len(a)])
    print("slice a[:len(a)]=",a[:len(a)])
    print("slice a[0:]=",a[0:])
    print("slice a[:]=",a[:])

    title("Slicing with steps")
    # specify steps for a slice [first_index:last_index:step]
    print("slice a[::1]=",a[::1])
    print("slice a[::2]=",a[::2])
    print("slice a[::3]=",a[::3])
    
    print("slice a[0:len(a):1]=",a[0:len(a):1])
    print("slice a[0:len(a):2]=",a[0:len(a):2])
    print("slice a[0:len(a):3]=",a[0:len(a):3])

    title("Slicing with Negative steps(from right to left)")
    # specify Negative steps for a slice [last_index:first_index:-step]
    #   it slices list from right to left (reverse)
    print("slice a[::-1]=",a[::-1])
    print("slice a[::-2]=",a[::-2])
    print("slice a[::-3]=",a[::-3])
    print("slice a[len(a):0:-1]=",a[len(a):0:-1])
    print("slice a[len(a):0:-2]=",a[len(a):0:-2])
    print("slice a[len(a):0:-3]=",a[len(a):0:-3])

    # Negative Slicing
    title("Negative Slicing")
    comment("a[-len(a):] ia the same as a[0:len(a)]")
    print("slice a[-len(a):]=",a[-len(a):])
    # slice last 4 items
    print("slice a[-4:]=",a[-4:])
    # slice last 3 items before last item -->
    comment("a[-4:-1] doesn't include last item --> 7,8,9 not have 10")
    print("slice a[-4:-1]=",a[-4:-1])
    # NOTE: add length of list to every negative index to get the positive index
    # -1  + 10 = 9
    # -2  + 10 = 8
    # -3  + 10 = 7
    # -4  + 10 = 6
    # -5  + 10 = 5
    # -6  + 10 = 4
    # -7  + 10 = 3
    # -8  + 10 = 2
    # -9  + 10 = 1
    # -10  + 10 = 0
    # at slicing [first : last]
    # first is considered the normal negative indexing
    # but the last is the index of the item next to last item in slice
    # so in negative last slice indexing :
    # -1 is the item before the last one
    # so to slice last item at last index by negative indexing:
    comment("slice only last")
    print("slice a[-1:]=",a[-1:])
    comment("slice last two items")
    print("slice a[-2:]=",a[-2:])
    comment("slice last three items")
    print("slice a[-3:]=",a[-3:])
    comment("slice items from 3 to 6 by negative index")
    print("slice a[-7:-3]=",a[-7:-3])
    print("slice a[3:7]=",a[3:7])

    # negative slicing with normal (positive) steps
    comment("negative slicing with normal (positive) steps")
    print("slice a[-10:-1:1]=",a[-10:-1:1])
    print("slice a[-10::1]=",a[-10::1])

    print("slice a[-10:-1:2]=",a[-10:-1:2])
    print("slice a[-10::2]=",a[-10::2])

    comment("negative slicing with right to left (negative) steps")
    # negative slicing with right to left (negative) steps
    print("slice a[-1:-10:-1]=",a[-1:-10:-1])
    print("slice a[-1:-11:-1]=",a[-1:-11:-1])

    comment(" with positive start and negative end")
    print("slice a[0:-1]=[0:9]=",a[0:-1])
    print("slice a[0:-2]=[0:8]=",a[0:-2])
    print("slice a[0:-3]=[0:7]=",a[0:-3])
    print("slice a[3:-3]=[3:7]=",a[3:-3])

    comment(" with negative start and positive end")
    print("slice a[-10:10]=[0:10]=",a[-10:10])
    print("slice a[-9:10]=[1:10]=",a[-9:10])
    print("slice a[-10:1]=[0:1]=[0]=[-10]=",a[-10:1])

    title("assigning to slices")
    name = list("perl")
    print("name =",name)
    name[2:] = list("ee")
    print("assign slice[2:] to value 'ee':")
    print("name =",name)

    comment("assign with different length")
    name = list("python")
    print("name =",name)
    name[1:] = list("erl")
    print("assign slice[1:] to value 'erl':")
    print("name =",name)
    name[1:] = list("ython")
    print("assign slice[1:] to value 'ython':")
    print("name =",name)

    comment("insert by slices")
    n = [1,5]
    print("n =",n)
    n[1:1] = [2,3,4]
    print("insert by slice n[1:1] values [2,3,4]")
    print("n =",n)

    comment("delete by slices")
    n = [1,2,3,4,5]
    print("n =",n)
    n[1:4] = []
    print("delete by slice n[1:4] values [2,3,4]")
    print("n =",n)

    comment("append by slices")
    n = [1,2,3,4]
    print("n =",n)
    n[len(n):] = list(range(5,10))
    print("append values n[len(n):] = [5,6,7,8,9]")
    print("n =",n)
    
    title("Multiply and concate lists ")
    print("[1,2,3,4,5] + [6,7,8,9,10] =",[1,2,3,4,5] + [6,7,8,9,10])
    print("[1,2,3,4,5] * 2 =",[1,2,3,4,5] * 2)
    print("'Python' * 3 =","Python" * 3)
    print("'python' + 'java' =","python" + "java")
    print("[42] * 10 =",[42] * 10)
    print("[None] * 10 =",[None] * 10)

    title("Membership in operator")
    print('"M" in "Moamen" =',"M" in "Moamen")
    print('"mm" in "Mohammed" =',"mm" in "Mohammed")
    print("1 in [4,5,6,1,2,3,6] =",1 in [4,5,6,1,2,3,6])
    print("2 in [4,5,6,1,2,3,6] =",2 in [4,5,6,1,2,3,6])
    print("3 in [4,5,6,1,2,3,6] =",3 in [4,5,6,1,2,3,6])
    print("7 in [4,5,6,1,2,3,6] =",7 in [4,5,6,1,2,3,6])

    # Important Note:
    # strings is immutable but list is mutable, so if we
    # want to manipulate with string and change it's content,
    # we should convert it to list by using list() function
    # and this is different than string.replace() function as
    # it returns new string with the new replaced characters
    title("Use list() function to convert string to mutable list")
    s1 = "Moamen Soroor"
    ls1 = list(s1)
    print("s1 =",s1)
    print("ls1 =",ls1)
    ls1.reverse()
    print("reversed ls1 =",ls1)
    ls1.sort()
    print("sorted ls1 =",ls1)
    ls1.remove("M")
    print("remove M from ls1 =",ls1)

    title("use lists as Stack - FILO - structure")
    stack = []
    stack.append("aaa")
    print("stack.append('aaa') =", stack)
    stack.append("bbb")
    print("stack.append('bbb') =", stack)
    stack.append("ccc")
    print("stack.append('ccc') =", stack)
    
    print("stack.pop() =", stack.pop())
    print("stack.pop() =", stack.pop())
    print("stack.pop() =", stack.pop())

    title("use lists as Queue - FIFO - structure")
    queue = []
    queue.append("aaa")
    print("queue.append('aaa') =", queue)
    queue.append("bbb")
    print("queue.append('bbb') =", queue)
    queue.append("ccc")
    print("queue.append('ccc') =", queue)
    
    print("queue.pop(0) =", queue.pop(0))
    print("queue.pop(0) =", queue.pop(0))
    print("queue.pop(0) =", queue.pop(0))

    title("Different Ways to initiate a list")
    ls1 = []
    print("ls1 = [] -->",ls1)
    ls1 = [0,1,2,3,4]
    print("ls1 = [0,1,2,3,4] -->",ls1)
    ls1 = list(range(0,5))
    print("list(range(0,5)) -->",ls1)
    ls1 = list(range(0,10,2))
    print("list(range(0,10,2)) -->",ls1)
    ls1 = list(range(5,0,-1))
    print("list(range(5,0,-1)) -->",ls1)
    ls1 = list(range(10,0,-2))
    print("list(range(10,0,-2)) -->",ls1)
    
    ls1 = list(reversed([10,20,30,40]))
    print("list(reversed([10,20,30,40]) -->",ls1)
    print("##### another way to reverse")
    ls1 = list([10,20,30,40][::-1])
    print("list([10,20,30,40][::-1]) -->",ls1)

    ls1 = list(sorted([40,20,100,50, 60 , 10]))
    print("list(sorted([40,20,100,50, 60 , 10])) -->",ls1)

    print('sorted("python") =' ,sorted("python"))
    
    # sorted with key
    
    
    
    
    

list_training()
