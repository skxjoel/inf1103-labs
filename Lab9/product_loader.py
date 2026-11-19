import csv
from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip the header row
            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type, product_id, name,
                                                    float(price), int(stock), supplier)
                    inventory.add_product(product)
                except ValueError as e:
                    print(f"Skipping row {row_number} {row}: {e}")
                    continue
                loaded += 1
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")