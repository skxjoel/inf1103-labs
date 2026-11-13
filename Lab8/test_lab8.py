from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def make_products() -> tuple[PhysicalProduct, DigitalProduct]:
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 5, supplier, 2.1)
    ebook = DigitalProduct("D001", "Python eBook", 30.00, 100, supplier, 15.0)
    return laptop, ebook


def test_association() -> None:
    print("\n--- Section 2: association (Supplier - Product) ---")
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 5, supplier, 2.1)
    ebook = DigitalProduct("D001", "Python eBook", 30.00, 100, supplier, 15.0)
    laptop.get_supplier().display_information()
    ebook.get_supplier().display_information()
    print("Both products share one Supplier object:",
          laptop.get_supplier() is ebook.get_supplier())
    del supplier  # Predict first: can the products still show their supplier?
    print("After del supplier:")
    laptop.get_supplier().display_information()
    ebook.get_supplier().display_information()


def test_aggregation() -> None:
    print("\n--- Section 3: aggregation (Inventory - Product) ---")
    laptop, _ = make_products()          # product exists before any inventory
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(laptop)
    inventory_a.remove_product("P001")
    print("Found in A after removal:", inventory_a.find_product("P001"))
    print("Product still usable after removal:")
    laptop.display_information()
    inventory_b.add_product(laptop)
    print("Same object now in B:", inventory_b.find_product("P001") is laptop)


def test_composition() -> None:
    print("\n--- Section 4: composition (Order - OrderLine) ---")
    laptop, ebook = make_products()
    order_1 = Order("O001")
    order_1.add_order_line(laptop, 1)
    order_1.add_order_line(ebook, 2)
    order_1.display_order()
    order_2 = Order("O002")
    order_2.add_order_line(laptop, 3)
    line_1 = order_1.get_order_lines()[0]
    line_2 = order_2.get_order_lines()[0]
    print("Same OrderLine object in both orders:", line_1 is line_2)
    print("Same Product object in both lines:", line_1.get_product() is line_2.get_product())
    order_1.remove_order_line("D001")
    print("After removing the eBook line:")
    order_1.display_order()


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_lsp() -> None:
    print("\n--- Section 6: LSP ---")
    laptop, ebook = make_products()
    show_product_details(laptop)
    show_product_details(ebook)
    for product in (laptop, ebook):
        product.update_stock(50)   # same call, same meaning for both subclasses
        product.display_information()


def test_polymorphism() -> None:
    print("\n--- Section 7: polymorphism ---")
    laptop, ebook = make_products()
    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(ebook)
    for product in inventory.get_products():
        product.display_information()
        print(product.get_fulfilment_info())


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp()
    test_polymorphism()
