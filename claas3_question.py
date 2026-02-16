#q1 
"""movies=[]
a=input("enter your first movie")
b=input("enter your second movie")
c=input("enter your third movie")
movies.append(a)
movies.append(b)
movies.append(c)
print(movies)"""
# alternative
"""movies=[]
movies.append(input("enter your first movie"))
movies.append(input("enter your second movie"))
movies.append(input("enter your third movie"))
print(movies)"""
#q2 palindrome
list1=[1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
#q3
"""list=["c","d","a","a","b","b","a"]
print(list.count("a"))"""
#q4
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)
