import re
str = 'an example word:bean!!'
match = re.search(r'word:\w\w\w\w', str)
if match:
    print('found', match.group()) #'found word:cat'
else:
    print('did not find')
