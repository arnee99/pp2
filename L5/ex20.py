def f(): 
    print(s)
   
    # This program will NOT show error
    # if we comment below line. 
    s = "Me too."
   
    print(s)
   
# Global scope
s = "I love Geeksforgeeks"
f()
print(s)