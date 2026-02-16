"""str="Apna college" #slicing
print(str[1:4])
print(str[:4]) #[0:4]
print(str[1:])#[1:len(str)]
print(str[-4:-1])"""
str="i am coder"
print(len(str)) #length of str
print(str.endswith("er")) #returns true if string ends with substr
str=str.capitalize()
print(str.capitalize()) #capitalize 1st char
print(str.replace("coder","learner")) #for replace substr
print(str.find("coder")) #returns 1st index of word
print(str.count("am")) #count the occurence of substr
print(str.count("e")) #count the occurence of substr

