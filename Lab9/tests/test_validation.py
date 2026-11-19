import pytest
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine
from inventory import Inventory

SUPPLIER = Supplier("S001", "TechSource", "sales@techsource.com")


@pytest.mark.parametrize("price", [0, -1, -0.01])
def test_price_must_be_positive(price):
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        PhysicalProduct("P001", "Lamp", price, 1, SUPPLIER, 1.0)


def test_stock_cannot_be_negative():
    with pytest.raises(ValueError, match="Stock quantity cannot be negative"):
        DigitalProduct("D001", "Editor", 10.0, -1, SUPPLIER, 100)


def test_zero_stock_is_allowed():
    assert PhysicalProduct("P001", "Lamp", 10.0, 0, SUPPLIER, 1.0).get_stock() == 0


@pytest.mark.parametrize("cls,extra", [(PhysicalProduct, 1.0), (DigitalProduct, 100)])
def test_update_stock_rule_is_same_for_every_subclass(cls, extra):
    # LSP: subclasses keep the parent's stock rule
    product = cls("X001", "Item", 10.0, 5, SUPPLIER, extra)
    with pytest.raises(ValueError):
        product.update_stock(-1)
    assert product.get_stock() == 5


@pytest.mark.parametrize("quantity", [0, -3])
def test_order_line_quantity_must_be_positive(quantity):
    lamp = PhysicalProduct("P001", "Lamp", 10.0, 5, SUPPLIER, 1.0)
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        OrderLine(lamp, quantity)


def test_inventory_rejects_duplicate_ids():
    inventory = Inventory()
    inventory.add_product(PhysicalProduct("P001", "Lamp", 10.0, 5, SUPPLIER, 1.0))
    with pytest.raises(ValueError, match="already exists"):
        inventory.add_product(DigitalProduct("P001", "Other", 5.0, 1, SUPPLIER, 10))
