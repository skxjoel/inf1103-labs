from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def get_discount(self) -> DiscountStrategy:
        return self.__discount

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return

    def calculate_total(self) -> float:
            total = sum(line.calculate_subtotal() for line in self.__order_lines)
            return self.__discount.apply(total)

    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        for order_line in self.__order_lines:
            order_line.display_information()
        print(f"    Total: ${self.calculate_total():.2f}")