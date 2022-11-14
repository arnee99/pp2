# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
 
from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
# 1 -> 5 & 8
# 2 -> 8 & 10
# 3 -> 10 & 20
# ...
print(sum)  