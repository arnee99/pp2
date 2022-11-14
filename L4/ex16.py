# Python3 program to show that we can create
# instance variables inside methods
 
# Class for Dog
 
class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed):
 
        # Instance Variable
        self.breed = breed
 
    #getter & setter from Java
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
 
    # Retrieves instance variable
    def getColor(self):
        return self.color
 
 
# Driver Code
Rodger = Dog("bulldog")
Rodger.setColor("brown")
print(Rodger.getColor())