# write a program  wheteher number is prime or not 
n=int(input("Enter a number :"))
for i in range(2,n):
    if(n%i) == 0:
        print("the number not  prime")
        break
else:
        print("the number is prime")
        # this code is not proper work