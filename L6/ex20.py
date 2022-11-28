# Python program to demonstrate
# strftime() function
 
from datetime import datetime as dt
 
# Getting current date and time
now = dt.now()
print("Without formatting", now)
 
# Example 1
s = now.strftime("%A %m %-Y")
print('\nExample 1:', s)
 
# Example 2
s = now.strftime("%a %-m %y")
print('\nExample 2:', s)
 
# Example 3
s = now.strftime("%-I %p %S")
print('\nExample 3:', s)
 
# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)