# Python program to illustrate
# *args for variable number of arguments
 
def myFun(*argv):
    for arg in argv:
        print(arg) 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')