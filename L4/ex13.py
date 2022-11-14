# Python3 program to
# demonstrate instantiating
# a class
class Dog:
 
    # A simple class
    # attribute
    attr1 = "mammal" #млекопитающее
    attr2 = "dog"
 
    # A sample method
    # this in C++ / Java
    def fun(self):
        print('Something!')
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
#print(Rodger.attr1)
#print(Rodger.attr2)
Rodger.fun()