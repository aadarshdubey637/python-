# write a python program to rempve a given word from a list ad strip it at thhe same time 


'''def rem(l,word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
        
l=["Aadarsh","Mnavi","Rohan","Shubham","an"]
print(rem(l,"an"))'''

def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
l=["Aadarsh","Manvi","Rohan","an"]
print(rem(l,"an"))