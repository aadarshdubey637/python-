# write a program to print 1 to 20 table genrate from  thee folder and folder name is tables 

def generatetable(n):
    table=" "
    for i in range(1,11):  
        table +=f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generatetable(i)    