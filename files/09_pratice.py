# write a program to find out whether a file is identical & matches the content of another files

with open("myfiles.txt")as f:
    content1=f.read()

with open("this_copy.txt")as f:
    content2=f.read()
if(content1==content2):
    print("yes this files are identicl ") 
else:
    print("no this files are not identical")     