def knapsack(N, K, items):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        W, V = items[i-1]
        for w in range(1, K + 1):
            if w >= W:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-W] + V)
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N][K]

# 입력 받기
N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# 배낭 문제 해결
result = knapsack(N, K, items)
print(result)
