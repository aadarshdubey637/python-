#self contructor ek method hoti hai jo object banate time automatically  call  hota hh  

# class employee:
#     language="python"
#     salary=1200

#     def __init__(self):
#         print("I am creating an object")

# something=employee()
# print(something.language,something.salary)        

# other way 
class employee:
    language="python"
    salary=1200

    def __init__(self,name,language,salary):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

something=employee("aadarsh",12000,"javascript")        
print(something.name,something.language,something.salary)