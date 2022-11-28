from datetime import datetime as dt
 
# Getting current date and time
now = dt.now()
 
string = dt.isoformat(now)
print(string)
print(type(string))