# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value
 
# An iterable user defined type
class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value of x
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
        
        #raise -> return error state
 
        # Else increment and return old value
        self.x = x + 1
        return x
 
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)
#[10;15]
 
# Prints nothing
for i in Test(5):
    print(i)
# 5 in not in [10;...)