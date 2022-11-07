# python code to demonstrate working of reduce()
# with a lambda function
 
# importing functools for reduce()
import functools
 
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))