#while conditions
"""i = 1
while i <= 5:
    print("hello")
    i+=1"""
#q1
"""i=1
while i <= 100:
    print(i)
    i+=1"""
#q2
"""i=100
while i >= 1:
    print(i)
    i-=1"""
#q3
"""n=int(input("enter the n"))
i=1
while i <= 10:
    m=n*i
    i+=1
    print(m)"""
#q4
"""nums = [1,4,9,16,25,36,49,64,81,100]
 
idx=0 
while idx < len(nums) :
    print(nums[idx])
    idx += 1"""
#q5
"""nums = (1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i< len(nums):
    if(nums[i] == x):
        print("index found at",i)
        break
    i+=1"""
#for loop
"""nums = [1,2,3,4,5]
for i in nums:
    print(i)
else:
    print("end") 
    """
#Q1  
"""nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)
"""
#q2
"""nums = (1,4,9,16,25,36,49,64,81,100)
x=25
for i in nums:
    if(i==x):
        print("found ")
        break
else: 
     print("not found")
"""
# range
"""for i in range(5):
    print(i)"""
#range(start,stop,step)
"""for i in range(2,51,2):
    print(i)"""
#q1
"""for i in range(1,101):
    print(i)"""
#q2
"""for i in range(100,0,-1):
    print(i)
    """
#q3
"""n=int(input("enter n :"))
for i in range(1,11):
    print(n*i)"""
#pass null statement that does nothing 
"""for i in range(5):
    pass"""
#q1
"""n=int(input("enter the n :"))
i=1
sum =0
while i <= n:
    sum +=i
    i+=1
print("sum :",sum)"""
#q2

n=int(input("enter the n :"))
i=1
fact =1
while i <= n:
    fact *=i
    i+=1
print("fact :",sum)