T = int(input())

N = [ int(input()) for _ in range(T) ]

dp = [ (0,0) for _ in range(max(N)+1) ]

for i in range(max(N)+1):
    if i == 0:
        dp[i] = (1, 0)
        continue
    if i == 1:
        dp[i] = (0, 1)
        continue
    dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])

for j in N:
    print(dp[j][0], dp[j][1])