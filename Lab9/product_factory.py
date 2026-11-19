class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier, extra: float = 0.0) -> Product:
        product_type = product_type.strip().lower()
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, extra)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier, extra)
        else:
            raise ValueError(f"Unknown product type: {product_type}")