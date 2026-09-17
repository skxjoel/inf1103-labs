
inventory = 0
total_units = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        print("Total Units Processed:", total_units)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    inventory += stock
    total_units += stock

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break
    else:
        print("Current inventory:", inventory)