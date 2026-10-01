ORDERS_FILE = "orders.txt"
FIRST_ORDER_ID = 1001
 
 
def load_orders():
    """Returns a list of (order_id, product, quantity). Starts empty if the file is missing or unreadable."""
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


def next_order_id(orders):
    """Returns the next unused order ID."""
    if not orders:
        return FIRST_ORDER_ID
    return max(order_id for order_id, _, _ in orders) + 1


def add_order(orders, product, quantity):
    """Creates a new order, appends it to the list, and returns it."""
    order = (next_order_id(orders), product, quantity)
    orders.append(order)
    return order


def save_orders(orders):
    """Writes all orders to the orders file, one per line."""
    with open(ORDERS_FILE, "w") as f:
        for order_id, product, quantity in orders:
            f.write(f"{order_id},{product},{quantity}\n")


def main():
    orders = load_orders()
    display_orders(orders)

    product = get_valid_product()
    quantity = get_valid_quantity()

    order_id, product, quantity = add_order(orders, product, quantity)
    print("\nNew Order Added:")
    print(f"{order_id},{product},{quantity}")

    save_orders(orders)
    print(f"\nOrder successfully saved to {ORDERS_FILE}")

    
if __name__ == "__main__":
    main()