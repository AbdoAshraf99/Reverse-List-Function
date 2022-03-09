def FunReverse (list1) :
    list1.reverse()

def Rev(list1):
    return[ele for ele in reversed(list1)]

def ReverseFunction(list1):
    new_list1 =list1[::-1]
    return new_list1
mylist = [5,7,2,9]
lis = [8,4,7,3]
RFlist = [12,55,47,41.0]
FunReverse(mylist)
print(mylist)
print(Rev(lis))
print(ReverseFunction(RFlist))