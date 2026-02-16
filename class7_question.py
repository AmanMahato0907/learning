#q1
"""with open("demo.txt","w") as f:
    f.write("hi everyone \n we are learning file I/O\n")
    f.write("using java.\n i like programing in java.")"""
#q2
"""with open("demo.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)
with open("demo.txt","w") as f:
    f.write(new_data)"""
#q3
"""
word = "learning"
with open("demo.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
"""
#q4
"""def chk_for_line():
    word = "learning"
    data = True
    line_no =1
    with open ("demo.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1
chk_for_line()
"""
#q5
count=0
with open ("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count +=1
print(count)
