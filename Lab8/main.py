import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from product import Product
from supplier import Supplier

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
      if item["type"] == "physical":
          return PhysicalProduct(item["product_id"], item["name"], item["price"],
                                 item["stock"], supplier, item["weight"])
      elif item["type"] == "digital":
          return DigitalProduct(item["product_id"], item["name"], item["price"],
                                item["stock"], supplier, item["download_size"])
      raise ValueError(f"Unknown product type: {item['type']}")


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
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            supplier = ask_for_supplier()
            if ptype == "1":
                weight = float(input("Weight (kg): "))
                inventory.add_product(PhysicalProduct(pid, name, price, stock, supplier, weight))
            else:
                size = float(input("Download size (MB): "))
                inventory.add_product(DigitalProduct(pid, name, price, stock, supplier, size))
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
            pid = input("Product ID to remove: ")
            if inventory.find_product(pid) is not None:
                inventory.remove_product(pid)
                print("Product removed from inventory.")
            else:
                print("Product not found.")
        elif choice == "7":
            break


def ask_for_supplier() -> Supplier:
      supplier_id = input("Supplier ID: ")
      if supplier_id in suppliers:
          return suppliers[supplier_id]
      name = input("Supplier name: ")
      contact_email = input("Supplier contact email: ")
      return get_or_create_supplier(supplier_id, name, contact_email)


if __name__ == "__main__":
      main()