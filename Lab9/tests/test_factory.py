import pytest
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory

SUPPLIER = Supplier("S001", "TechSource", "sales@techsource.com")


def test_factory_creates_physical_product():
    product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, SUPPLIER, 1.2)
    assert isinstance(product, PhysicalProduct)
    assert isinstance(product, Product)


def test_factory_creates_digital_product():
    product = ProductFactory.create("digital", "D001", "Editor", 49.9, 100, SUPPLIER, 300)
    assert isinstance(product, DigitalProduct)


def test_factory_ignores_case_and_spaces():
    assert isinstance(ProductFactory.create(" Physical ", "P1", "A", 1, 1, SUPPLIER),
                      PhysicalProduct)


def test_unknown_type_raises_clear_value_error():
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", "S001", "Install", 30.0, 5, SUPPLIER)


def test_main_uses_factory_not_concrete_classes():
    from pathlib import Path
    source = (Path(__file__).resolve().parent.parent / "main.py").read_text()
    assert "PhysicalProduct(" not in source
    assert "DigitalProduct(" not in source
    assert "ProductFactory.create(" in source
