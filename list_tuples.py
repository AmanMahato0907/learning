"""list=["aman",0,89.9]
print(list[0])
print(list)
print(len(list))
print(type(list))
list[0]="amit" # muttable means it can be chnage
print(list)
print(list[0:2]) #slicing
"""
#list method
"""list=[2,1,3] 
list.append(4) # add one ele at the end
print(list)
list.sort() # sort the list
print (list)
list.sort(reverse=True) # sort the list in desc
print(list)
list.reverse() # reverse the list
print(list)
list.insert(0,0) # insert ele at index (ind,ele)
print(list)
list.remove(1) # remove first occurence of ele
print(list)
list.pop(1) # remove ele at ind
print(list)"""

#tuples immutable  
"""tup =(1,2,3,4)
print(tup)
print(tup[0])
t=() #tuple
tp=(1,) # without , it acts as data types
print(type(tp))
print(tup[1:3])"""
#tuples method 
tup=(2,1,3,1)
print(tup.index(3)) # return index of first occurence
print(tup.count(1))#count total occunre