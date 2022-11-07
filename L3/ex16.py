def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20
    print(x)
 
 
# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun(x)
print(x)