# mutable default argument values example using python list
 
# itemName is the name of the item that we want to add to list
# that is being passed, or if it is not passed then appending in
# the default list
 
def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList
 
 
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))