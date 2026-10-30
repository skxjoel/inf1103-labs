class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return
        self.__stock = quantity

    def display_information(self):
        print(f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | Stock: {self.__stock}")

    # Controlled read access, so other code never touches the __attributes
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def to_dict(self):
        return {"product_id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}