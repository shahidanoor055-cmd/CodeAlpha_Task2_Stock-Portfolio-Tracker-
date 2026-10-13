stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 180,
    "MSFT": 420
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("Stock Price:", price)
    print("Quantity:", quantity)
    print("Total Investment Value:", total_investment)
else:
    print("Stock not found in the list.")
    