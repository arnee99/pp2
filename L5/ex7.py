# Function to check object
# is iterable or not
def it(ob):
  try:
      iter(ob)
      return True
  except TypeError:
      return False
 
# Driver Code
for i in [34, [4, 5], (4, 5),
{"a":4}, "dfsdf", 4.5]:
 
    print(i,"is iterable :",it(i))