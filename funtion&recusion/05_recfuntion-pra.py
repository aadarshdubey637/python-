# write a program to convert inches to cms

def inc_to_cms(inch):
    return inch*2.54

n=int(input("Enter value of inches :"))
print(f"the corresponding value in cms is {inc_to_cms(n)}")