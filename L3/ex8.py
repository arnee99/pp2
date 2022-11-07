# using None as values of the default arguments
 
print('#list')
def appendItem(itemName, itemList=None):
    if itemList == None:
          itemList = []
    itemList.append(itemName)
    return itemList
 
 
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))
 
 
# using None as value of default parameter

print('\n\n#dictionary')
def addItemToDictionary(itemName, quantity, itemList = None):
    if itemList == None:
        itemList = {}
    itemList[itemName] = quantity
    return itemList
 
 
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))
