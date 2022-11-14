# A simple generator for Fibonacci Numbers
def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object
x = fib(5)
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
 
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)