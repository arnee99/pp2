# Python program to
# demonstrate date class
 
# import the date class
from datetime import date
 
# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)
 
print("Date passed as argument is", my_date)
 
# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range
 
# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of integer