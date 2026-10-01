# Constant variables
ORDERS_FILE = "orders.txt"
FIRST_ORDER_ID = 1001
 
 
def load_orders():
    """Returns a list of (order_id, product, quantity). 
    Starts empty if the file is missing or unreadable."""
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8-sig") as f:
            lines = f.read().splitlines()
        orders = []
        for line in lines:
            if not line.strip():
                continue
            order_id, product, quantity = line.split(",")
            orders.append((int(order_id), product.strip(), int(quantity)))
        return orders
    except FileNotFoundError:
        return []
    except ValueError:
        print("Warning: orders file is corrupted. Starting empty.")
        return []



def display_orders(orders):
    """Prints every saved order."""
    print("Current Orders:\n")
    if not orders:
        print("(no orders yet)")
    for order_id, product, quantity in orders:
        print(f"{order_id}, {product}, {quantity}")
    print()



def get_valid_product():
    """Keeps asking until a non-empty product name without commas is entered."""
    while True:
        product = input("Enter Product Name: ").strip()
 
        if not product:
            print("Error: Product name cannot be empty.")
        elif "," in product:
            print("Error: Product name cannot contain commas.")
        else:
            return product


def get_valid_quantity():
    """Keeps asking until a positive integer is entered."""
    while True:
        user_input = input("Enter Quantity: ")
 
        try:
            quantity = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
 
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            continue
 
        return quantity       


def main():
    orders = load_orders()
    display_orders(orders)

    product = get_valid_product()
    quantity = get_valid_quantity()

if __name__ == "__main__":
    main()