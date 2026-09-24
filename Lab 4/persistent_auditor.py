INVENTORY_FILE = "inventory.txt"


def load_inventory():
    """Returns (total, history). Starts empty if the file is missing or unreadable."""
    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8-sig") as f:
            lines = f.read().splitlines()
        total = int(lines[0])
        history = []
        if len(lines) > 1 and lines[1].strip():
            history = [int(x) for x in lines[1].split(",")]
        return total, history
    except FileNotFoundError:
        return 0, []
    except (ValueError, IndexError):
        print("Warning: inventory file is corrupted. Starting empty.")
        return 0, []


def get_valid_input():
    """Returns (value, failed_attempts_added)."""
    while True:
        user_input = input("Enter stock quantity (or type 'quit'): ")

        if user_input.lower() == "quit":
            return "quit", 0

        try:
            value = int(user_input)

            if value < 0:
                print("Error: Negative numbers are not allowed.")
                return None, 1

            return value, 0

        except ValueError:
            print("Error: Please enter a valid integer.")
            return None, 1


def process_delivery(current_total, new_value):
    """Adds the new delivery to the running total."""
    return current_total + new_value


def calculate_tax(amount):
    """Returns 10% tax for this delivery."""
    return amount * 0.10


def generate_report(total_units, deliveries_processed, failed_attempts):
    """Prints the final report."""

    print("\n===== Inventory Report =====")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory, history = load_inventory()
    print(f"Loaded inventory: {total_inventory} units, {len(history)} past transactions")
    deliveries_processed = 0
    failed_attempts = 0

    while True:
        result, failed_attempt = get_valid_input()
        failed_attempts += failed_attempt

        if result == "quit":
            break

        if result is None:
            continue

        tax = calculate_tax(result)
        total_inventory = process_delivery(total_inventory, result)
        deliveries_processed += 1

        print(f"Delivery accepted: {result}")
        print(f"Tax for this delivery: {tax:.2f}")
        print(f"Current inventory: {total_inventory}\n")

        if total_inventory > 500:
            print("ALERT: Inventory exceeds 500 units!")
            break

    generate_report(total_inventory, deliveries_processed, failed_attempts)


if __name__ == "__main__":
    main()