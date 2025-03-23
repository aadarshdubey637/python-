# write a class train which has method to book a ticket,get  status (no of seats)
 # and get fare information of train runiing under indian railway

from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo =trainNo
    
    def book(self,fro,to):
        print(f"Train is booked in traun no :{self.trainNo} from {fro} to {to}")


    def getstatus(self):
        print(f"Train no {self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(222,45444)}")

t=train(123999)
t.book("Bhopal","indore")
t.getstatus() 
t.getfare("Bhopal","Indore")      