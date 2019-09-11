
from basic0 import head
from basic0 import comment
from basic0 import title
from basic0 import qoute_str

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




