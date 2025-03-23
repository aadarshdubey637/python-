 # create a class with attribute a; create an objecyt from it and set 'a' directly using object a=o.does this change this class attribute

class demo:
    a = 4

o=demo() # print the class attribute because instance attribute is not present  
print(o.a)
o.a=0  # instance attribute is set
print(o.a) # print the instance attribute because instance attribute is present
print(demo.a)  # print the class attribute