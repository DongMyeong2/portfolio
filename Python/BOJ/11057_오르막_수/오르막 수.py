N = int(input())

dp = [ 1 for _ in range(10) ]

for _ in range(N):
    for n in range(1, 10):
        dp[n] += dp[n-1]

print(dp[-1]%10007)