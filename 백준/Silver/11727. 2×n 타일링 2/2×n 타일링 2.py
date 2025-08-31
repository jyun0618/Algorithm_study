MOD = 10007
n = int(input())

if n == 1:
    print(1)
else:
    dp1, dp2 = 1, 3  # dp[1], dp[2]
    if n == 2:
        print(dp2 % MOD)
    else:
        for _ in range(3, n + 1):
            dp1, dp2 = dp2, dp2 + 2 * dp1
        print(dp2 % MOD)
