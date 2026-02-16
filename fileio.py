#f=open("demo.txt", "r")
#data =f.read() #entire line
#print(data)
"""line1=f.readline() #one line

print(line1)
f.close()"""
"""f=open("demo.txt", "w")
f.write("hello i am aman mahato.")
f.close()
f=open("demo.txt", "a")
f.write("\n i am learning phython from apna college.")
f=open("demo.txt", "r")
data =f.read(

)
print(data)
f.close()"""
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
    #to remove a file
import os
os.remove("demo.txt")