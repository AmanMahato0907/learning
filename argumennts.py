## Positional arguments
"""def postional(a,b):
    print(a+b)
postional(10,20)
#keyword arguments
def keyword(a,b):
    print("Sum :",a+b)
keyword(b=32,a=10)
#default arguments
def default(a,b=10):
    print(a*b)
default(5)
default(5,4)"""
## Variable length arguments
# def var_length(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print("Sum :",sum)
# var_length(10,20,30)
# var_length(5,15,25,35,45)
# def show_details(name,*marks):
#     print("Name :",name)
#     print("Marks:",marks)
# show_details("Aman",90,76,43)
# def find_max(*args):
#     max_value=args[0]
#     for nums in args:
#         if nums> max_value:
#             max_value=nums
#     print("maximum value: ",max_value)
# find_max(10,342,1541,14)
# def sum(*add):
#     total=0
#     for i in add:
#         total+=i
#     print("total :",total)
# sum(102,332,1,2)
# num=[10,20,3,21]
# def find_max(*args):
#     max_val=args[0]
#     for i in args:
#         if i >max_val:
#             max_val=i
#     print("max_value",max_val)
# find_max(*num)
# def demo(x,*args):
#     print(len(args))
#     print(args[1])
# demo(10,20,30,40)
#**kwargs
# def sd(**kwargs):
#     print(kwargs)
# sd(name="aman",age=20,course="python")
# def sd(**kwargs):
#     print("Name :",kwargs["name"])
#     print("Age:",kwargs["age"])
# sd(name="aman",age=20)
# def display(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# display(language="Python", level="Beginner")
data = {"a": 1, "b": 2, "c": 3}

for key, value in data.items():
    print(key, value)
