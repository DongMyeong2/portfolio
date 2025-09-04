N = int(input())

check = [0] + [ int(input()) for _ in range(N) ]

dp = [0] * (N +1)
dp[1] = check[1]

for i in range(2, N+1):
    if i == 2:
        dp[2] = check[1] +check[2]
    else:
        dp[i] = max(check[i]+check[i-1]+dp[i-3], dp[i-2]+check[i])

print(dp[N])