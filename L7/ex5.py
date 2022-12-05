import re
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
print(match)
match = re.search(r'igs', 'piiig') # not found, match == None
print(match)

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"
print(match)
## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
print(match)
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
print(match)