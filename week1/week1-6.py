# Step 1: Create a grocery and prices dictionary
prices = {
    'Apple': 0.89,
    'Banana': 0.39,
    'Bread': 2.50,
    'Chocolate': 1.50
}

# Step 2: Suppose the customer purchased 3 Apples, 2 Bananas, 4 Breads and 1 Chocolate
purchases = {
    'Apple': 3,
    'Banana': 2,
    'Bread': 4,
    'Chocolate': 1
}

total_cost = 0
print("Receipt:")
for item, quantity in purchases.items():
    cost = prices[item] * quantity
    total_cost += cost
    print(f"{item}: {quantity} x ${prices[item]:.2f} = ${cost:.2f}")

print(f"\nTotal Cost: ${total_cost:.2f}")

# Step 3: Enhance the code to take user inputs
print("\nEnhanced Version:")
purchases = {}
total_cost = 0

for item, price in prices.items():
    quantity = int(input(f"Enter the number of {item}s purchased: "))
    purchases[item] = quantity

print("\nReceipt:")
for item, quantity in purchases.items():
    cost = prices[item] * quantity
    total_cost += cost
    print(f"{item}: {quantity} x ${prices[item]:.2f} = ${cost:.2f}")

print(f"\nTotal Cost: ${total_cost:.2f}")