import json
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"

def load_inventory(filename):
    inventory = Inventory()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        for item in data:
            inventory.add_product(
                Product(item["product_id"], item["name"], item["price"], item["stock"]))
    except FileNotFoundError:
        print("No saved inventory found. Starting empty.")
    return inventory

def save_inventory(inventory, filename):
    data = [p.to_dict() for p in inventory.get_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved.")

def main():
    inventory = load_inventory(FILENAME)
    while True:
        print("\n1. Display all products\n2. Add a product\n3. Update stock"
              "\n4. Search for a product\n5. Save inventory\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            inventory.add_product(Product(pid, name, price, stock))
        elif choice == "3":
            pid = input("Product ID to update: ")
            results = inventory.search_product(pid)
            if results:
                results[0].update_stock(int(input("New stock quantity: ")))
            else:
                print("Product not found.")
        elif choice == "4":
            results = inventory.search_product(input("Search: "))
            for p in results:
                p.display_information()
            if not results:
                print("No matching products.")
        elif choice == "5":
            save_inventory(inventory, FILENAME)
        elif choice == "6":
            break
        else:
            print("Invalid option.")

main()