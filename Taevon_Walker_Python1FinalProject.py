#You are tasked with creating a simple inventory management system for a market. The system should allow users to add,
#update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.

#Functionality:
#Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
#Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
#View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
#Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
#Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.

#Project Structure:
#Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
#Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.
#Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category


inventory = []


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added to inventory.")


def update_item():
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Enter new details (press enter to keep current value):")

            new_price = input(f"New price ({item['price']}): ")
            if new_price:
                item["price"] = float(new_price)

            new_quantity = input(f"New quantity ({item['quantity']}): ")
            if new_quantity:
                item["quantity"] = int(new_quantity)

            new_category = input(f"New category ({item['category']}): ")
            if new_category:
                item["category"] = new_category

            print(f"Item '{name}' updated successfully.")
            return

    print(f"Item '{name}' not found in inventory.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(
                f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}, Category: {item['category']}")


def remove_item():
    name = input("Enter the name of the item to remove: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            return

    print(f"Item '{name}' not found in inventory.")


def search_by_category():
    category = input("Enter the category to search for: ")
    found_items = [item for item in inventory if item["category"].lower() == category.lower()]

    if found_items:
        print(f"\nItems in category '{category}':")
        for item in found_items:
            print(f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
    else:
        print(f"No items found in category '{category}'.")


def main():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()