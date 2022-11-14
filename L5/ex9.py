tup = ('a', 'b', 'c', 'd', 'e')
 
# creating an iterator from the tuple
tup_iter = iter(tup)
 
print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
    print(item)
 
    # break outside loop after iterating on 3 elements
    if index == 2:
        break
 
# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))