N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

dp = [0]*(N+1)

for n in range(1, N+1):
    rest = A[n-1] - B
    if rest > 0:
        if rest % C != 0:
            dp[n] = dp[n-1] + (rest//C) + 2
        else:
            dp[n] = dp[n-1] + (rest//C) + 1
    else:
        dp[n] = dp[n-1] + 1
    
print(dp[N])