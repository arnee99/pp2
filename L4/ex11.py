# python code to demonstrate working of reduce()
# with a lambda function
 
# importing functools for reduce()
from functools import reduce
 
# initializing list
lis = [1, 3, 5, 6, 2, 9]
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
# return 1 if 1 > 3 else return 3
# return 3 if 3 > 5 else return 5
# return 5 if 5 > 6 else return 6
print(reduce(lambda a, b: a if a > b else b, lis))