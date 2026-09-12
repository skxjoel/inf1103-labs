
inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        continue

    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        continue

    stock = int(stock)

    inventory += stock

    print("Current inventory:", inventory)
