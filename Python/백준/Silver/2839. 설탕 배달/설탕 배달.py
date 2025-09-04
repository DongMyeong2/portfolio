N = int(input())
dp = [N]*(N+1)

for i in range(3, N+1):
    if i == 3 or i == 5:
        dp[i] = 1
        continue
    if i >= 4 and dp[i-3] != N:
        dp[i] = min(dp[i], dp[i-3]+1)
    if i >= 6 and dp[i-5] != N:
        dp[i] = min(dp[i], dp[i - 5]+1)
if dp[N] == N:
    print(-1)
else:
    print(dp[N])