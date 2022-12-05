import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning/end of a WORD:

#x = re.findall(r"\bain", txt)
x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

