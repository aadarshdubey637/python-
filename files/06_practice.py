# write a program to mine a log file and find out whether it contain "pyhton".

with open("log.txt") as f:
    content=f.read()

if("python" in content ):
    print("yes python is present in content :")
else:
    print("No python is not present in contennt :")    