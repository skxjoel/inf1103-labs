import json
from inventory import Inventory
from product import Product
from product_factory import ProductFactory
from supplier import Supplier
from input_helpers import get_positive_float, get_non_negative_int, get_non_empty_str

from pathlib import Path
FILENAME = Path(__file__).parent / "inventory.json"

suppliers: dict[str, Supplier] = {}

def get_or_create_supplier(supplier_id: str, name: str, contact_email: str) -> Supplier:
      if supplier_id not in suppliers:
          suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)
      return suppliers[supplier_id]


def load_inventory(filename: str) -> Inventory:
    inventory = Inventory()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        for item in data:
            inventory.add_product(create_product(item))
    except FileNotFoundError:
        print("No saved inventory found. Starting empty.")
    except json.JSONDecodeError:
        print("Saved inventory file is corrupted. Starting empty.")
        inventory = Inventory()
    except (KeyError, ValueError) as e:
        print(f"Saved inventory has an invalid product ({e}). Starting empty.")
        inventory = Inventory()
    return inventory

def save_inventory(inventory: Inventory, filename: str) -> None:
    data = [p.to_dict() for p in inventory.get_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved.")


def create_product(item: dict) -> Product:
      s = item.get("supplier", {"supplier_id": "S000", "name": "Unknown supplier",
                                "contact_email": "unknown@example.com"})
      supplier = get_or_create_supplier(s["supplier_id"], s["name"], s["contact_email"])
      extra = item.get("weight", item.get("download_size", 0.0))
      return ProductFactory.create(item["type"], item["product_id"], item["name"],
                                   item["price"], item["stock"], supplier, extra)


def main() -> None:
    inventory = load_inventory(FILENAME)
    while True:
        print("\n1. Display all products\n2. Add a product\n3. Update stock"
        "\n4. Search for a product\n5. Save inventory\n6. Remove a product"
        "\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            ptype = input("Type (1 = Physical, 2 = Digital): ")
            if ptype not in ("1", "2"):
                print("Invalid product type.")
                continue
            pid = get_non_empty_str("Product ID: ")
            if inventory.find_product(pid) is not None:
                print("A product with that ID already exists.")
                continue
            name = get_non_empty_str("Name: ")
            price = get_positive_float("Price: ")
            stock = get_non_negative_int("Stock: ")
            supplier = ask_for_supplier()
            if ptype == "1":
                extra = get_positive_float("Weight (kg): ")
                product_type = "physical"
            else:
                extra = get_positive_float("Download size (MB): ")
                product_type = "digital"
            try:
                product = ProductFactory.create(product_type, pid, name, price,
                                                stock, supplier, extra)
            except ValueError as e:
                print(f"Product not added: {e}")
                continue
            inventory.add_product(product)
            print("Product added.")
        elif choice == "3":
            pid = input("Product ID to update: ")
            results = inventory.search_product(pid)
            if results:
                results[0].update_stock(get_non_negative_int("New stock quantity: "))
                print("Stock updated.")
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
            pid = input("Product ID to remove: ")
            if inventory.find_product(pid) is not None:
                inventory.remove_product(pid)
                print("Product removed from inventory.")
            else:
                print("Product not found.")
        elif choice == "7":
            break
        else:
            print("Invalid option, please choose 1-7.")


def ask_for_supplier() -> Supplier:
      supplier_id = get_non_empty_str("Supplier ID: ")
      if supplier_id in suppliers:
          return suppliers[supplier_id]
      name = get_non_empty_str("Supplier name: ")
      contact_email = get_non_empty_str("Supplier contact email: ")
      return get_or_create_supplier(supplier_id, name, contact_email)


if __name__ == "__main__":
      main()