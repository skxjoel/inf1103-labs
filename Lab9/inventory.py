from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def find_product(self, product_id: str) -> Product | None:
      for product in self.__products:
          if product.get_product_id() == product_id:
              return product
      return None


    def remove_product(self, product_id: str) -> None:
      product = self.find_product(product_id)
      if product is not None:
          self.__products.remove(product)


    def search_product(self, keyword: str) -> list[Product]:
        keyword = keyword.lower()
        return [p for p in self.__products
                if keyword == p.get_product_id().lower() or keyword in p.get_name().lower()]

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return
        for product in self.__products:
            product.display_information()

    def get_products(self) -> list[Product]:
        return list(self.__products)