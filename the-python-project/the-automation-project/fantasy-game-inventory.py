def displayInventory(inventory):
    counter = 0
    print("Inventory")
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        counter += v
    print("Total number of items: " + str(counter))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

stuff = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12
}

input_inventory = {
    "gold coin": 42,
    "rope": 1
}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
input_inventory = addToInventory(input_inventory, dragon_loot)
displayInventory(input_inventory)