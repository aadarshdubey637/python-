#leap year
 
year=int(input("Enter leap year "))
if(year % 4 == 0 and year % 100 !=0) or(year % 400==0):
    print(year,"it is leap year")
else:
    print(year,"it is not leap year")