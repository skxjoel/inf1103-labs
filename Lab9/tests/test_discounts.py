import inspect
import pytest
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import (DiscountStrategy, NoDiscount, PercentageDiscount,
                               BulkDiscount, StudentDiscount)


def make_order_of_250(discount=None) -> Order:
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    chair = PhysicalProduct("P001", "Chair", 125.0, 10, supplier, 3.0)
    order = Order("O001", discount)
    order.add_order_line(chair, 2)  # 2 x 125 = 250
    return order


def test_default_is_no_discount():
    assert make_order_of_250().calculate_total() == pytest.approx(250.0)


def test_bulk_discount_applies_at_threshold():
    assert make_order_of_250(BulkDiscount(200, 20)).calculate_total() == pytest.approx(230.0)


def test_bulk_discount_not_applied_below_threshold():
    assert BulkDiscount(200, 20).apply(199.99) == pytest.approx(199.99)


def test_set_discount_changes_strategy():
    order = make_order_of_250(BulkDiscount(200, 20))
    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == pytest.approx(225.0)


def test_new_strategy_works_without_changing_order():
    assert make_order_of_250(StudentDiscount()).calculate_total() == pytest.approx(237.5)


def test_order_has_no_discount_if_elif_logic():
    source = inspect.getsource(Order)
    for name in ("PercentageDiscount", "BulkDiscount", "StudentDiscount", "elif"):
        assert name not in source


def test_strategy_can_be_shared_between_orders():
    shared = PercentageDiscount(10)
    assert Order("A", shared).get_discount() is Order("B", shared).get_discount()


def test_discount_strategy_is_abstract():
    with pytest.raises(TypeError):
        DiscountStrategy()


def test_invalid_percentage_rejected():
    with pytest.raises(ValueError):
        PercentageDiscount(150)
