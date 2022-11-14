class A:
    def __init__(self, n='Mark'):
        self.name = n
 
 
class B(A):
    def __init__(self, roll, n='Mark'):
        self.roll = roll
        A.__init__(self, n)
    
    
 
 
object = B(23)
#object.roll = 23
#B -> A 
print(object.name)