def knapsack(n, W, items):
    # Initialize the table with zeros
    table = [[0 for x in range(W + 1)] for y in range(n + 1)]

    # Build the table in bottom-up fashion
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            weight = items[i - 1][0]
            value = items[i - 1][1]
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - weight] + value)

    # Return the maximum value
    return table[n][W]


# Read the number of instances
T = int(input())

# Iterate through each instance
for t in range(T):
    # Read the number of items and the capacity
    n, W = map(int, input().split())

    # Read the items
    items = []
    for i in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    # Calculate and print the maximum value
    print(knapsack(n, W, items))
