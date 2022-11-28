# Python program to
# demonstrate time class
 
from datetime import time
 
# calling the constructor
my_time = time(13, 24, 56)
 
print("Entered time", my_time)
 
# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)
 
# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)
 
# Uncommenting 
# my_time = time(hour = 26)
# will rase an ValueError as
# it is out of range
 
# uncommenting
# my_time = time(hour ='23')
# will raise TypeError as
# string is passed instead of int