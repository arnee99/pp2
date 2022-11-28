from datetime import time
 
# Creating Time object
Time = time(12,24,36,1212)
 
# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))