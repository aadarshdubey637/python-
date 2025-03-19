 #program to find largest of three number
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)