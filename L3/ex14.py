# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
 
 
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)