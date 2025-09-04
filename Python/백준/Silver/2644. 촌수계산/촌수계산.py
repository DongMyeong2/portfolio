def dfs(now, ans):
    if now == B:
        return ans
    for i in lst[now]:
        if not visited[i]:
            visited[i] = True
            result = dfs(i, ans + 1)
            if result is not None:
                return result
    return None

N = int(input())
A, B = map(int, input().split())
M = int(input())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [False] * (N + 1)
visited[A] = True

result = dfs(A, 0)
print(result if result is not None else -1)