# -*- 
from basic0 import head
from basic0 import comment
from basic0 import title
from basic0 import qoute_str
import copy
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
    # NOTE: values() return all values, keys() returns all keys ,
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

    comment("delete the dictionary from memory with it's items")
    del dic
    # ERROR: print(dic)
    # UnboundLocalError: local variable 'dic' referenced before assignment

    #initialize with constructor dict()
    comment("allocate dictionary dic with constructor dict()")
    dic = dict(fname = "moamen", lname = "soroor" ,
               age = 24 , hobby = "gaming")
    print("dic: " , dic)
    
    dic2 = dict(dic)
    print("dic: " , dic2)
    
    dic3 = dict(**dic)
    print("dic: " , dic3)

    # functions clear() copy() fromkeys() setdefault()
    # copy then clear()
    comment("copy() function")
    dic2 = dic.copy()
    comment("clear() function")
    dic.clear()
    print("cleared dic:",dic)

    comment("add items to dic again without new memory allocation(Object reference)")
    dic["fname"] = "moamen"
    dic["lname"] = "soroor"
    dic["age"] = 24
    print("dic: " , dic)
    # setdefault() function
    comment("setdefault() function")
    print('dic.setdefault("fname") =')
    print(dic.setdefault("fname"))
    print("dic:" , dic)
    print('dic.setdefault("lname" , "Gamal") =')
    print(dic.setdefault("lname" , "Gamal"))
    print("dic:" , dic)
    print('dic.setdefault("mname") =')      
    print(dic.setdefault("mname"))
    print("dic:" , dic)
    print('dic.setdefault("mname" , "Mohammed")')  
    print(dic.setdefault("mname" , "Mohammed"))
    print(dic)


    
    del dic , dic2
    print("delete dictionaries: dic and dic2")
    # print("dic: " , dic2)
    # print("dic1: " , dic)

    
    

    # Copy and Deep Copy
    title("Shallow copy and Deep Copy")
    # first shallow copy()
    comment("Shallow copy using dictionary.copy() function")
    dic = {"name": "admin" , "jobs": ["Engineer" , "Cooker" , "Teacher"]}
    dic2 = dic.copy()
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### change dic2 name: ")
    dic2["name"] = "Moamen"
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### remove dic2 cooker jobs: ")
    dic2["jobs"].remove("Cooker")
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### add dic2 Wooder jobs: ")
    dic2["jobs"].append("Wooder")
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### We can see copy is shallow copy")

    comment("Deep copy using copy.deepcopy(dictionary) function")
    # copy() is deep copy
    print("\n#### Let's see now deep copy, we should import copy module")

    dic = {"name": "admin" , "jobs": ["Engineer" , "Cooker" , "Teacher"]}
    dic2 = copy.deepcopy(dic)
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### change dic2 name: ")
    dic2["name"] = "Moamen"
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### remove dic2 cooker jobs: ")
    dic2["jobs"].remove("Cooker")
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### add dic2 Wooder jobs: ")
    dic2["jobs"].append("Wooder")
    print("dic =",dic)
    print("dic2 =",dic2)

    print("\n#### We can see copy is deep copy")



def find_phone_addrress():
    data = {
        "moamen" : {
            "phone" : "1234",
            "addr" : "Sers"
            },

        "shady" : {
            "phone" : "5678",
            "addr": "Cairo"
            },

        "kamal" : {
            "phone" : "9012",
            "addr": "Menouf"
            }
        }

    labels = {
        "phone" : "Phone Number",
        "addr" : "Address"
        }

    name = input("Name: ")
    if name.lower() == "exit": return name.lower()
    choose = input("Phone(p) or Address(a)? ")

    if choose == "p": key = "phone"
    elif choose == "a": key = "addr"
    else:
        print("ERROR: Error in Selection")
        return name.lower()

    if name in data :
        print("RESULT: {}'s {} is {}".format(name,labels[key],data[name][key]))
    else: print("RESULT: Name not Found")
    return name

def format_string_with_dic():

    txt =\
    """\
fname: {fname}
lname: {lname}
age: {age}
study: {study}\
"""
    txt_dict = {
        "fname": "Moamen",
        "lname": "Soroor",
        "age" : 24,
        "study" : "Engineering"
        }
    print(txt.format_map(txt_dict))
##  RESULT:
##  fname: Moamen
##  lname: Soroor
##  age: 24
##  study: Engineering

if basic05_dictionary.__name == "__main__":
    dictionary_training()
    #while find_phone_addrress() != "exit": pass
    #print("Program Ended Successfuly")
    format_string_with_dic()


















    

