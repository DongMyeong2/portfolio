def dfs(row):
    global ans
    if row == N:
        ans += 1
        return

    for col in range(N):
        if not columns[col] and not diagonal1[row - col] and not diagonal2[row + col]:
            # 퀸 배치
            columns[col] = diagonal1[row - col] = diagonal2[row + col] = True
            dfs(row + 1)
            # 백트래킹
            columns[col] = diagonal1[row - col] = diagonal2[row + col] = False

N = int(input())

# 배열 초기화
columns = [False] * N
diagonal1 = [False] * (2 * N - 1)
diagonal2 = [False] * (2 * N - 1)

ans = 0
dfs(0)
print(ans)
