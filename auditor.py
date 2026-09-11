inventory = 0

while True:
    user_input = input("Enter a stock quantity (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        break

    inventory += int(user_input)
    print(f"Current inventory: {inventory}")

print(f"Final inventory: {inventory}")