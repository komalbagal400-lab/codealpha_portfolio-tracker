stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2700, "MSFT": 330}

portfolio = {}

# Get user input for stocks and quantities
while True:
    stock_name = input("Enter stock symbol (or type 'done'): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be positive. Please try again.")
            continue
        portfolio[stock_name] = quantity
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate total investment value
total_value = 0
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} x ${price} = ${value}")

print(f"\nTotal investment value: ${total_value}")

# Optional: Save to a file
save_to_file = input("Save to file? (yes/no): ").lower()
if save_to_file == 'yes':
    filename = input("Enter filename (e.g., portfolio.txt): ")
    try:
        with open(filename, 'w') as f:
            f.write("Stock Portfolio\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                f.write(f"{stock}: {quantity} x ${price} = ${value}\n")
            f.write(f"\nTotal investment value: ${total_value}\n")
        print(f"Portfolio saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")
