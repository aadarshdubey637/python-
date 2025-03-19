# write a program to find out whether a student has passed or failed if it required a total of 40% and 
# atleast 33 in each subject to pass assumme 3 subject and take marks as an input from the user 

mark1=int(input("enter marks1 :"))
mark2=int(input("enter marks2 :"))
mark3=int(input("enter marks3 :"))

#check  for total percentage
total_perchentage = (100*(mark1 + mark2 + mark3))/300

if(total_perchentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are passed :",total_perchentage)
else:
    print("you are failed:",total_perchentage)

