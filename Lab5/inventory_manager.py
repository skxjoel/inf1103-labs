

import os
import json

FILENAME = "data/inventory.json"



def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


def search_product(inventory, product_id):
    for p in inventory:
        if p["id"].upper() == product_id.upper():
            return p
    return None


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if search_product(inventory, product_id):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid number entered. Product not added.")
        return
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = search_product(inventory, input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    try:
        product["stock"] = int(input("New Stock Quantity: "))
    except ValueError:
        print("Invalid number entered. Stock unchanged.")
        return
    print("Stock updated successfully!")


def print_product(product_id, inventory):
    print("Search Product")
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)


def load_inventory():
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        try:
            with open(FILENAME, "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Could not read inventory.json. Starting with empty inventory.")
            return []
    print("inventory.json not found. Starting with empty inventory.")
    return []


def save_inventory(inventory):
    print("Saving inventory...")
    with open(FILENAME, "w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved successfully to inventory.json.")

def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Enter option: ").strip()
        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            print("Search Product")
            pid = input("Enter Product ID: ").strip()
            print_product(pid, inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()