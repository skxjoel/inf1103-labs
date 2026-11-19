import pytest
from inventory import Inventory
from supplier import Supplier
from product_loader import load_products
from input_helpers import get_positive_float, get_non_negative_int

SUPPLIER = Supplier("S000", "CSV Import", "import@example.com")
CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


def fake_input(monkeypatch, answers):
    answers = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))


def test_get_positive_float_retries_until_valid(monkeypatch, capsys):
    fake_input(monkeypatch, ["abc", "-5", "12.50"])
    assert get_positive_float("Price: ") == 12.50
    out = capsys.readouterr().out
    assert "Please enter a valid number, e.g. 12.50" in out
    assert "Please enter a number greater than zero." in out


def test_get_non_negative_int_retries_until_valid(monkeypatch):
    fake_input(monkeypatch, ["ten", "-1", "0"])
    assert get_non_negative_int("Stock: ") == 0


def test_bad_rows_skipped_and_valid_rows_load(tmp_path, capsys):
    path = tmp_path / "products.csv"
    path.write_text(CSV_TEXT)
    inventory = Inventory()
    load_products(str(path), inventory, SUPPLIER)
    out = capsys.readouterr().out
    assert [p.get_product_id() for p in inventory.get_products()] == ["P001", "D001", "P003"]
    assert "Unknown product type: service" in out
    assert "3 products loaded." in out
    assert out.strip().endswith("Load attempt finished.")


def test_missing_file_handled_gracefully(tmp_path, capsys):
    inventory = Inventory()
    load_products(str(tmp_path / "nope.csv"), inventory, SUPPLIER)
    out = capsys.readouterr().out
    assert "Products file not found" in out
    assert "products loaded" not in out          # else block did not run
    assert "Load attempt finished." in out       # finally always runs
    assert inventory.get_products() == []


def test_each_except_is_specific():
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    for name in ("main.py", "product_loader.py", "input_helpers.py"):
        source = (root / name).read_text()
        assert "except:" not in source
        assert "except Exception" not in source
