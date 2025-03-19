# write a program to changed file name to another files

with open("this.txt")as f:
    content=f.read()

    with open("renamed_file.txt","w")as f:
        f.write(content) 