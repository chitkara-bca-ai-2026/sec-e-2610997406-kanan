inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("===== INVENTORY MENU =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Current Inventory:")
        for i, item in enumerate(inventory, 1):
            print(i, item)

    elif choice == "2":
        item = input("Enter item name: ")

        if item in inventory:
            print("Item already exists!")
        else:
            inventory.append(item)
            print("Item added successfully!")

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in inventory:
            inventory.remove(item)
            print("Item removed successfully!")
        else:
            print("Item not found!")

    elif choice == "4":
        inventory.sort()
        print("Inventory sorted alphabetically!")
        print(inventory)

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
