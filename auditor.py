
inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        continue

    stock = int(stock)
    inventory = stock

    print("Stock quantity:", inventory)
