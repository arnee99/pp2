# This function modifies global variable 's'
def f():
    global s
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)
   
# Global Scope
s = "Python is great !"
f()
print(s)