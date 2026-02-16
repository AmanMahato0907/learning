"""age=int(input("Enter your age"))
if(age >= 18):
    print("Eligible to vote.")
else:
    print("Not Eligible to vote.")"""
marks=int(input("enter yours marks"))
if(marks>=90):
    print("Grade=A")
elif(90>marks>=80): #or (marks>=80 and marks<90):
    print("Grade=B")
elif(80>marks>=70):
    print("Grade=C")
elif(marks<70):
    print("Grade=D")