def get_valid_input():
    """Gets user input, validates it, and returns an integer or 'quit'."""
    while True:
        user_input = input("Enter stock quantity (or type 'quit'): ")

        if user_input.lower() == "quit":
            return "quit"

        try:
            value = int(user_input)

            if value < 0:
                print("Error: Negative numbers are not allowed.")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid integer.")

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
    
    total_inventory = 0
    deliveries_processed = 0
    failed_attempts = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        tax = calculate_tax(result)
        total_inventory = process_delivery(total_inventory, result)
        deliveries_processed += 1


        generate_report(total_inventory, deliveries_processed, failed_attempts)


if __name__ == "__main__":
    main()
    # if inventory > 500:
    #     print("ALERT: Overstock! Inventory exceeds 500 units.")
    #     break
    # else:
    #     print("Current inventory:", inventory)