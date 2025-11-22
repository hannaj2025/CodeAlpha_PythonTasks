# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "META": 310
}

portfolio = {}
total_value = 0

print("📊 Stock Portfolio Tracker")

n = int(input("How many stocks do you want to add? "))

for _ in range(n):
    name = input("Enter stock symbol (AAPL/TSLA/GOOG/META): ").upper()
    qty = int(input("Enter quantity: "))

    if name in stock_prices:
        portfolio[name] = portfolio.get(name, 0) + qty
    else:
        print("Stock not found!")

# Calculate total value
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    print(f"{stock}: {qty} shares → ₹{value}")
    total_value += value

print("\n💰 Total Investment Value:", total_value)

# Optional save
save = input("Save result to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares → ₹{qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Value: ₹{total_value}")

    print("📁 Saved to portfolio.txt")
