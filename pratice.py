(1) #calculate area of circle
import math
radius=float(input("enter radius:"))
area= math.pi*radius**2
print("area of the cicle is",area)

(2) temprature in kelvin
celsius=float(input("enter temprature in celcius"))
kelvin=celsius+273.15
print("temprature in kelvin",kelvin)

(2)#miles is equal to km
miles=float(input("enter miles:"))
km=miles/0.621371
print(miles," miles is eual to",km,"kilometer")

(3) #leap year

year=int(input("eneter leap year"))
if(year % 4 == 0 and year %100 !=0) or(year % 400 ==0):
print(year,"it is leap year")
else:
    print(year,"it is not")

(4) #swap two value
a=input("enter a")
b=input("enter b")
a,b=b,a
print("After swaping,a=",a,"b=",b,)

(5)#  calculate simple interst
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)


