"""#dict
info={
    "name": "Aman",
    "age" : 12,
    "subjects":["python","c","java"]

}
print(info)
print(info["name"])
print(info["age"])
info["name"]="aman"
info["surname"]="mahato"
print(info)"""
 #nested dict
"""student = {
    "name" :"aman",
    "subjects" : {
        "phy" : 75,
        "che" : 89,
        "math" : 81
    }
} 
print(student)
print(student["subjects"]["phy"])
# dict method
print(student.keys()) # return all keys
print(len(student)) # len of dict
print(list(student.values())) # return all values
print(list(student.items())) # return all (keys,values)items
print(student["name"])
print(student.get("name")) # returns keys acc to values
student.update({"city":"delhi"}) #inserted the specified to the dict
print(list(student.items()))"""
# sets
null_set=set() #empty set
print(null_set)
collection={1,2,3,3,4,4,4} # ignore duplicate values
print(collection)
print(len(collection))
collection.add(5) # add values in set
print(collection)
collection.remove(5) # remove values from sets
print(collection)
collection.clear() #clear set
print(collection)
collection={1,2,3,3,4,4,4} # ignore duplicate values
print(collection.pop()) # pop random values
col={5,6,7,1,2}
print(collection.union(col))
print(collection.intersection(col))
