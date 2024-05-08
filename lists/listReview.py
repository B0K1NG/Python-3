inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Using length
inventory_len = len(inventory)
print(inventory_len)

#Selecting first element
first = inventory[0]
print(first)

#Selecting last element
last = inventory[-1]
print(last)

#Selecting items from inventory starting index 2 and up to, but not including 6
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#Saving first 3 items of inventory
first_3 = inventory[:3]
print(first_3)

#Counting twin beds in inventory
twin_beds = inventory.count("twin bed")
print(twin_beds)

#Removing 5th element from inventory
removed_item  = inventory.pop(4)
print(removed_item)

#Inserting new item
inventory.insert(10, "19th Century Bed Frame")

#Sorting the inventory
inventory.sort()
print(inventory)