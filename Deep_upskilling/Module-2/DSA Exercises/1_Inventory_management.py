class Product:

    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price

    def display(self):
        print(self.pid, self.name, self.qty, self.price)


inventory = {}

while True:

    print("\n1.Add 2.Update 3.Delete 4.View 5.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        pid = int(input("Product ID: "))
        name = input("Product Name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))

        inventory[pid] = Product(pid, name, qty, price)

    elif choice == 2:

        pid = int(input("Enter Product ID: "))

        if pid in inventory:
            inventory[pid].qty = int(input("New Quantity: "))

    elif choice == 3:

        pid = int(input("Enter Product ID: "))
        inventory.pop(pid, None)

    elif choice == 4:

        for item in inventory.values():
            item.display()

    else:
        break