def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


def search_product(inventory, product_id):
    for p in inventory:
        if p["id"].upper() == product_id.upper():
            return p
    return None


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if search_product(inventory, product_id):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid number entered. Product not added.")
        return
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = search_product(inventory, input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    try:
        product["stock"] = int(input("New Stock Quantity: "))
    except ValueError:
        print("Invalid number entered. Stock unchanged.")
        return
    print("Stock updated successfully!")


def print_product(product_id, inventory):
    print("Search Product")
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)



def main():
    inventory = [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]
    display_all(inventory)
    add_product(inventory)
    update_stock(inventory)
    print_product(input("Enter Product ID: "), inventory)
    display_all(inventory)
    

if __name__ == "__main__":
    main()