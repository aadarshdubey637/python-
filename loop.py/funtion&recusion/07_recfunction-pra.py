# write a program to calculate multipilication of table using funtion 
def multiply(n):
    for i in range(1,11):
        print(f" {n} x {i} = {n*i}")


n=int(input("Enter value : "))
print(multiply(n))