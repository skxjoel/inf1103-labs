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



def main():
    orders = load_orders()



if __name__ == "__main__":
    main()