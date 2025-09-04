N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
dp = [ [0]*N for _ in range(N) ]
direction = [ [0,1], [1,0] ]
dp[0][0] = 1
for row in range(N):
    for col in range(N):
        if row == N-1 and col == N-1:
            break
        if dp[row][col] >= 1:
            for dx, dy in direction:
                if row+(dx*arr[row][col]) < N and col+(dy*arr[row][col]) < N:
                    dp[row+dx*arr[row][col]][col+dy*arr[row][col]] += dp[row][col]
print(dp[N-1][N-1])