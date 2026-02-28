# Day 42 - Longest Common Subsequence (LCS)


# 1️⃣ Recursive (Basic Understanding)
def lcs_recursive(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0

    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    else:
        return max(
            lcs_recursive(s1, s2, m - 1, n),
            lcs_recursive(s1, s2, m, n - 1)
        )


# 2️⃣ DP Tabulation
def lcs_dp(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# -------- Testing --------

s1 = "abcde"
s2 = "ace"

print("LCS Recursive:", lcs_recursive(s1, s2, len(s1), len(s2)))
print("LCS DP:", lcs_dp(s1, s2))
