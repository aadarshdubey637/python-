class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name :{self.name},age:{self.age}")


person1=person("Aadarsh",14)
person1.display()
        