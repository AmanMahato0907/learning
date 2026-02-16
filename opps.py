"""class Student:
    name="Karan Kumar"
s1=Student()
print(s1.name)"""

"""class Car:
    color="blue"
    model="SUV"
c1=Car()
print(c1.color,"\n",c1.model)"""
#constructor
class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database ..")
s1 = Student("aman")
print(s1.name)
s2=Student("bidha")
print(s2.name)