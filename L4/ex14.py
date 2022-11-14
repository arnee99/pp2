# Sample class with init method
class Person:
 
    # init method or constructor
    #Person.__init__(self, name)
    def __init__(self, name):
        #In a current function we only talk about data of an obejct
        #that has called a constructor
        #self -> object p
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Abc')
p.say_hi()