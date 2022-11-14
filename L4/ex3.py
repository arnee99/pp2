is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#[...]
# 1 * 10
# 2 * 10
# 3 * 10
# 4 * 10
 
# iterate on each lambda function
# and invoke the function to get the calculated value
#for item in is_even_list:
for i in is_even_list:
    print(i())

print(is_even_list[0]())