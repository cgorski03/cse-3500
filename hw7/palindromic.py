def longestPalindromeSubseq(s):
    n = len(s)
    # Create a 2D table to store the lengths of the LCS
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[n - j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the length of the longest palindromic subsequence
    return dp[n][n]


def myLongest(s):
    n = len(s)
    # Create a 2D table to store the lengths of the LCS
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[n - j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the length of the longest palindromic subsequence
    return dp[n][n]


print(longestPalindromeSubseq("character"))
