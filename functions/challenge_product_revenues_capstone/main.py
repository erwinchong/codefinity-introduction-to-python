def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(revenues):
    temp_revenues = sorted(revenues)
    for k, v in temp_revenues:
        print(f"{k} has total revenue of ${v}.")


products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))

formatted_output(revenue_per_product)