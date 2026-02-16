"""l=[10,20,30,40,100,200,300,400]
def multiply(n):
    return n*10
print(list(map(multiply,l)))
data=[2,None,4,6,8,None,-10] #print using map and lambda print  numbers and none  None=list(filter(lambda x: x is not None, data))
none=list(filter(lambda x: x is not None, data))
print(none)
l=[10,20,30,40,100,200,3000,400]
import functools
print(functools.reduce(lambda x,y: x if x>y else y,l))"""
import functools
data = [2, None, -3, 4, 0, 5]
result = functools.reduce(lambda x, y: x *y,filter(lambda x: x is not None and x>0,data))
print(result)



