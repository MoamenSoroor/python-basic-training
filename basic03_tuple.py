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
#========================= tuple training =========================
#==================================================================
def tuple_training():
    head("tuple training")
    t1 = ("moamen" , "mohammed" , "gamal" , "soroor")
    print("tuple t1 =",t1)
    print("tuple t1 type =",type(t1))
    print("tuple t1 length =",len(t1))
