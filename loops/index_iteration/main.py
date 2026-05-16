prices = [29.99, 45.50, 12.75, 38.20]

discount_percentage = [10, 20, 15, 5]

for i in range(len(prices)):
    new_price = prices[i] * (1 - discount_percentage[i] / 100)
    prices[i] = new_price
    print(f"Updated price for item {i}: ${new_price:.2f}")