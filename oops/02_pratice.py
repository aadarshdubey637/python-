# Write a class "calculator" capable of finding sqaure ,cube and sqaure root of a number   

class calculator:
    def __init3__(self,n):
        self.n=n

    def square(self):
        print(f"The square is : {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"The squareroot  is : {self.n**0.5}")

num=float(input("Enter a number :"))
a=calculator(num)
a.square()
a.cube()
a.squareroot()
            
        