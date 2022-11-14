# Python program to illustrate destructor
class Employee:
    
    # Initializing
    def __init__(self, name):
        self.name = name
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee('Mark')
print(obj.name)
del obj