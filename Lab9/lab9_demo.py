import os
import shutil
from pathlib import Path
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from inventory import Inventory
from product_factory import ProductFactory
from product_loader import load_products
from discount_strategy import BulkDiscount, PercentageDiscount, StudentDiscount

HERE = Path(__file__).parent
SUPPLIER = Supplier("S001", "TechSource", "sales@techsource.com")


def section_2_strategy() -> None:
    print("\n--- Section 2.3: Strategy ---")
    chair = PhysicalProduct("P001", "Chair", 125.0, 10, SUPPLIER, 3.0)
    order = Order("O001", BulkDiscount(200, 20))
    order.add_order_line(chair, 2)                       # lines add up to 250
    print("BulkDiscount(200, 20):", order.calculate_total())
    order.set_discount(PercentageDiscount(10))
    print("After set_discount(PercentageDiscount(10)):", order.calculate_total())
    order.set_discount(StudentDiscount())
    print("After set_discount(StudentDiscount()):", order.calculate_total())

    print("\n--- Section 2.4: Order - DiscountStrategy ---")
    shared = PercentageDiscount(10)
    a, b = Order("A", shared), Order("B", shared)
    print("Two orders share one strategy object:", a.get_discount() is b.get_discount())


def section_3_factory() -> None:
    print("\n--- Section 3.2: Factory with an unknown type ---")
    try:
        ProductFactory.create("service", "S001", "Installation", 30.0, 5, SUPPLIER)
    except ValueError as e:
        print("ValueError raised:", e)
    print("(Without this try/except the program would stop with a traceback.)")


def section_5_load() -> None:
    print("\n--- Section 5.2: load_products with products.csv ---")
    load_products(str(HERE / "products.csv"), Inventory(), SUPPLIER)

    print("\n--- Section 5.2: load_products after renaming products.csv ---")
    renamed = HERE / "products_renamed.csv"
    shutil.move(HERE / "products.csv", renamed)
    try:
        load_products(str(HERE / "products.csv"), Inventory(), SUPPLIER)
    finally:
        shutil.move(renamed, HERE / "products.csv")      # put the file back


if __name__ == "__main__":
    section_2_strategy()
    section_3_factory()
    section_5_load()
