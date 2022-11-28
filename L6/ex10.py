from datetime import date
   
# calling the today
# function of date class
today = date.today()
   
# Converting the date to the string
Str = date.isoformat(today)
Str2 = today.strftime("%Y/%m/%d")
print("String Representation #1", Str)
print("String Representation #2", Str2)
print(type(Str))