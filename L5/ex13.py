# Python code to demonstrate the working of
# dropwhile() and filterfalse()
 
# importing "itertools" for iterator operations
import itertools
 
# initializing list
li = [2, 4, 5, 7, 8]
 
# using dropwhile() to start displaying after condition is false
print ("The values after condition returns false : ",end="")
print (list(itertools.dropwhile(lambda x : x%2==0,li)))
 
# using filterfalse() to print false values
print ("The values that return false to function are : ",end="")
print (list(itertools.filterfalse(lambda x : x%2==0,li)))