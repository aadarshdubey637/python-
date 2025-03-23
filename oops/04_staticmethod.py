#.m   static method me self parameter ki jarurat nahi hoti
class calculator:
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
result1=calculator.add(10,5)
result2=calculator.multiply(10,5)
print("Addition is :",result1)
print("Multiply is :",result2)
