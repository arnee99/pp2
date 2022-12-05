# A Simple Python program to demonstrate working
# of yield
 
# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
 
def simpleGeneratorFun():
    yield 1
    #function stops
    #yield send a value "1" -> go back to a function and continue execution
    yield 2
    #yield send a value "2" -> go back to a function and continue execution
    yield 3
    #yield send a value "3" -> go back to a function and continue execution
    #some actions
 
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)