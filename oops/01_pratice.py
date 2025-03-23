# create a class "programmer" for storing information of few programmer working at microsoft


class programmer:
    company="Microsoft"
   
    def __init__(self,name,salary,pin):
         self.name=name
         self.salary=salary
         self.pin=pin

p=programmer("Aadarsh",12000,464668)
print(p.name,p.company,p.pin,p.salary)