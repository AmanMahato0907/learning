#functions : block of code that perform specific task.
# def func_name(parm1,parm2):
#some work
#return val
#func_name(arg1,arg2) <-func call

"""def calc_sum(a,b):
    s=a+b
    print(s)
    return s
calc_sum(2,5)
calc_sum(7,8)"""

"""def calc_avg(a,b,c):
    avg=(a+b+c)/3
    return avg
m=int(input("enter 1st marks:"))
n=int(input("enter 2nd marks:"))
o=int(input("enter 3 rd marks:"))
print("average marks :",calc_avg(m,n,o))"""
#q1
"""cities = ["delhi","jamshedpur","noida","ranchi","bokaro"]
heroes= ["ironman","hulk","black widow","dr.strange"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)"""
#q2
"""
def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(heroes)"""
#q3
"""
def fact_no(n):
    fact=1
    for i in range(1,n+1,1):
        fact =fact*i      
    print(fact)

fact_no(9)"""
#q4
"""
def u_i(u):
    inr=u*87
    print("usd value :",inr, "inr")
u_i(10)"""
#Q5
def e_o(n):
    if((n%2) == 0):
        print("EVEN")
    else:
        print("ODD")
i=int(input("enter the number:"))
e_o(i)
