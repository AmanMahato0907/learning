#recursion -> when a function call itself repeatedly
"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)"""
"""def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n* fact(n-1)
    
print(fact(5))"""
#q1
"""
def nat(n):
    if(n==0):
        return 0
    return nat(n-1)+n
print(nat(10))"""
#q2
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","apple","banana"]
print_list(fruits)
print 