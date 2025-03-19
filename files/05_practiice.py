# repeat program 4 for a list of such words to be consored
words = ["donkey","bad","poor"]

with open("donkey.txt","r")as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" *len(word))

with open("donkey.txt","w")as f:
    f.write(content)

