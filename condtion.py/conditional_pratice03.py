 # a spam comment is defined as a last conversing follpwing keywords "make a lot of money","buy now","subscribe this","click this" write a program to detect these spanned

p1="make a lot of money"
p2="buy now"
p3="go there"
p4="click this"

message=input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment  is spam :")
else:
    print("this comment is not spam.!")
#print("end the program..!")