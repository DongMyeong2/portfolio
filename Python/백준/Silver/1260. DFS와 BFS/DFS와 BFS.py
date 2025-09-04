def dfs(now):
    if dfs_check[now]:
        return
    dfs_result.append(now)
    dfs_check[now] = 1
    for i in range(len(arr[now])):
        dfs(arr[now][i])

def bfs(start):
    bfs_check[start] = 1
    que = [start]
    while que:
        now = que.pop(0)
        bfs_result.append(now)
        for i in range(len(arr[now])):
            if bfs_check[arr[now][i]] == 0:
                que.append(arr[now][i])
                bfs_check[arr[now][i]] = 1

N, M, V = map(int, input().split())

arr = [ [] for _ in range(N+1) ]

dfs_result = []
dfs_check = [ 0 ] * (N+1)

bfs_result = []
bfs_check = [ 0 ] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N+1):
    arr[i].sort()

dfs(V)
bfs(V)
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))