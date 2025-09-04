def bfs():
    visited = [0] * (N + 1)
    # 전체 순열 사이클
    result = []
    # 한 순열 사이클

    for i in range(1, N+1):
        sub = []
        if visited[i]:
            continue
        que = [i]
        while True:
            if not que:
                result.append(sub)
                break
            now = que.pop(0)
            for i in range(len(lst[now])):
                if visited[lst[now][i]] == 0:
                    que.append(lst[now][i])
                    sub.append(lst[now][i])
                    visited[lst[now][i]] = 1
    return len(result)

T = int(input())

for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    lst = [ [] for _ in range(N+1) ]

    for i in range(N):
        lst[i+1].append(num[i])
        lst[num[i]].append(i+1)

    print(bfs())