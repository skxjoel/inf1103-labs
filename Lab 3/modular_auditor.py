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

inventory = 0
total_units = 0
failed_entries = 0

def main():
    total_inventory = 0
    deliveries_processed = 0
    failed_attempts = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break
        
        total_inventory += result
        deliveries_processed += 1

    # if inventory > 500:
    #     print("ALERT: Overstock! Inventory exceeds 500 units.")
    #     break
    # else:
    #     print("Current inventory:", inventory)