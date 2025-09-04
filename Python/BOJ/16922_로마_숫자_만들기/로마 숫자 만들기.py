def dfs(n, sm):
    if n == N:
        result.add(sm)
        return

    if (n, sm) in memo:
        return
    memo.add((n, sm))

    for x in num:
        dfs(n + 1, sm + x)


N = int(input())
num = (1, 5, 10, 50)
result = set()
memo = set()

dfs(0, 0)
print(len(result))