# Day 41 - 0/1 Knapsack Problem (Dynamic Programming)


# 1️ Recursive Solution (Basic Understanding)
def knapsack_recursive(weights, values, W, n):
    if n == 0 or W == 0:
        return 0

    if weights[n - 1] > W:
        return knapsack_recursive(weights, values, W, n - 1)

    else:
        include = values[n - 1] + knapsack_recursive(
            weights, values, W - weights[n - 1], n - 1
        )
        exclude = knapsack_recursive(weights, values, W, n - 1)

        return max(include, exclude)


# 2️ DP Tabulation Solution
def knapsack_dp(weights, values, W):
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# -------- Testing --------

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Knapsack Recursive:", knapsack_recursive(weights, values, capacity, len(weights)))
print("Knapsack DP:", knapsack_dp(weights, values, capacity))
