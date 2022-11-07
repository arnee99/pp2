# Sample class with init method
class Person:
 
    # init method or constructor
    #Person.__init__(self, name)
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()