# Python code to demonstrate the working of
# accumulate() and chain()
 
# importing "itertools" for iterator operations
import itertools
 
# importing "operator" for operator operations
import operator
 
# initializing list 1
li1 = [1, 4, 5, 7]
 
# initializing list 2
li2 = [1, 6, 5, 9]
 
# initializing list 3
li3 = [8, 10, 5, 4]
 
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ",end="")
print (list(itertools.accumulate(li1)))
 
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ",end="")
print (list(itertools.accumulate(li1,operator.mul)))
 
# using chain() to print all elements of lists
print ("All values in mentioned chain are : ",end="")
print (list(itertools.chain(li1,li2,li3)))