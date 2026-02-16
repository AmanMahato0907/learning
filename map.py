# l=[10,20,2,1,102]
# def multiply(n):
#     return n*10
# print(list(map(multiply,l)))
#print(set(map(lambda n:n*10,[10,20,2,1,102])))
# l=[10,20,2,1,102]
# print(type(list(map(int,l))))
# l=list(map(int,input().split("-")))
# print(l)
l=[11,22,33,10,78,23]
# def is_even(n):
#     return n%2==0
# print(list(filter(is_even ,l)))
import functools as ftools # aliasing
print(ftools.reduce(lambda a,b:a+b,l))