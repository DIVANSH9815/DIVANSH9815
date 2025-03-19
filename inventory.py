class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name] > quantity:
                self.items[name] -= quantity
            else:
                del self.items[name]
        else:
            print("Item not found!")

    def show_inventory(self):
        for item, qty in self.items.items():
            print(f"{item}: {qty}")

# Example Usage
inv = Inventory()
inv.add_item("Laptop", 5)
inv.add_item("Mouse", 10)
inv.add_item("Laptop", 3)
inv.remove_item("Mouse", 5)

inv.show_inventory()
