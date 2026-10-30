class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, keyword):
        keyword = keyword.lower()
        return [p for p in self.__products
                if keyword == p.get_product_id().lower() or keyword in p.get_name().lower()]

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        for product in self.__products:
            product.display_information()

    def get_products(self):
        return list(self.__products)