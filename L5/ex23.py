# Python program to demonstrate
# nonlocal keyword
 
print ("Value of a using nonlocal is : ", end ="")
def outer():
    a = 5
    def inner():
        nonlocal a 
        a = 10
    inner()
    print (a)
   
outer()
   
# demonstrating without non local 
# inner loop not changing the value of outer a
# prints 5
print ("Value of a without using nonlocal is : ", end ="")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print (a)
   
outer()