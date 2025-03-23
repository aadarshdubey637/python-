# self parameter is a special parameter that is use to instance method  when you  define method inside of class is a first parameter each method take
 
# self represents the current instance of the class.
class employee:
    language="pyhton"
    salary=12000

    def getinfo(self):
      print(f"The language is :{self.language}.The salary is {self.salary} ")
    
    @staticmethod
    def greet():
       print("good moprning")  


aadarsh = employee()
aadarsh.getinfo()
aadarsh.greet()
# print(aadarsh.language,aadarsh.salary)
# employee.getinfo(aadarsh)