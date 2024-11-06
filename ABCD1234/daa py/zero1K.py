def knapsack(weights, values, capacity):
    n = len(values)
    # Create a 2D array to store maximum values at each n and capacity
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Identify included items
    included_items = [0] * n
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item is included
            included_items[i - 1] = 1
            w -= weights[i - 1]

    return dp[n][capacity], included_items

def main():
    n = int(input("Enter number of items: "))
    weights = [int(input(f"Item {i + 1} weight: ")) for i in range(n)]
    values = [int(input(f"Item {i + 1} value: ")) for i in range(n)]
    capacity = int(input("Enter knapsack capacity: "))

    import time
    start_time = time.perf_counter()

    max_value, included_items = knapsack(weights, values, capacity)

    end_time = time.perf_counter()

    print(f"Maximum value in Knapsack: {max_value}")
    print(f"Items included (1) / Excluded (0): {included_items}")
    print(f"Time taken: {(end_time - start_time) * 1000:.6f} ms")

if __name__ == "__main__":
    main()
