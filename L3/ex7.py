# mutable default argument values example using python dictionary
 
# itemName is the name of item and quantity is the number of such
# items are there
 
def addItemToDictionary(itemName, quantity, itemList = {}):
    itemList[itemName] = quantity
    return itemList
 
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))