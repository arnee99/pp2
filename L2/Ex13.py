i = 0
a = 'geeksforgeeks'
  
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
          
    print('Current Letter :', a[i])
    i += 1