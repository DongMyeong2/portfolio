N, M = map(int, input().split())
arr = [[0]*M] + [ list(map(int, input().split())) for _ in range(N)]
dp = [ [0] * M for _ in range(N+1) ]

for row in range(1, N+1):
    for col in range(M):
        if col == 0:
            dp[row][col] = arr[row][col] + dp[row-1][col]
        else:
            dp[row][col] = arr[row][col] + max(dp[row-1][col], dp[row][col-1])
print(dp[N][M-1])