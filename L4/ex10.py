# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
 
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)  