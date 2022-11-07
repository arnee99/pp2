is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
 
# iterate on each lambda function
# and invoke the function to get the calculated value
#for item in is_even_list:
for item in is_even_list:
    print(item())