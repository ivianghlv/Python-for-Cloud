# Student A: Define the Item class representing an item in the inventory
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

# Student B: Define the Inventory class representing the inventory system
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                break

    def total_value(self):
        return sum(i.total_cost() for i in self.items)

# Student C: Write a test function
def test_inventory_system():
    inv = Inventory()
    items = [
        Item("Butter Cookies", 50, 5),
        Item("Sweet Tarts", 100, 2),
        Item("Chocolate Cookies", 65, 3)
    ]
    
    for item in items:
        inv.add_item(item)    
    print("Total Inventory Value:", inv.total_value())

# Student D: Runs the inventory
if __name__ == "__main__":
    test_inventory_system()
