def fractional_knapsack(weights, profits, capacity):
    ratios = [(profits[i] / weights[i], weights[i], profits[i], i + 1) for i in range(len(weights))]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_profit = 0.0
    remaining_capacity = capacity
    selected_items = []

    for ratio in ratios:
        ratio_value, weight, profit, item = ratio
        if remaining_capacity == 0:
            break

        weight_to_take = min(weight, remaining_capacity)
        remaining_capacity -= weight_to_take
        total_profit += (weight_to_take / weight) * profit
        selected_items.append(item)

    return total_profit, selected_items


n = int(input("Enter the number of items: "))
weights = []
profits = []

for i in range(n):
    weight = float(input(f"Enter the weight of item {i + 1}: "))
    profit = float(input(f"Enter the profit of item {i + 1}: "))
    weights.append(weight)
    profits.append(profit)

capacity = float(input("Enter the capacity of the knapsack: "))

max_profit, selected_items = fractional_knapsack(weights, profits, capacity)

print(f"\nThe maximum profit is: {max_profit:.2f}")
print(f"Knapsack selected items: {{ {', '.join(map(str, selected_items))} }}")