# Day 43 - Coin Change (Minimum Coins)


# 1️⃣ Recursive (Basic Understanding)
def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')

    for coin in coins:
        result = coin_change_recursive(coins, amount - coin)
        if result != float('inf'):
            min_coins = min(min_coins, 1 + result)

    return min_coins


# 2️⃣ DP Bottom-Up (Optimal)
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # 0 amount needs 0 coins

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1


# -------- Testing --------

coins = [1, 2, 5]
amount = 11

print("Recursive:", coin_change_recursive(coins, amount))
print("DP:", coin_change_dp(coins, amount))
