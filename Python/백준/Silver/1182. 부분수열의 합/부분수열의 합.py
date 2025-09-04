def dfs(n,check):
    global ans
    if n == N:
        if sum(check) == S and len(check) > 0:
            ans += 1
        return
    dfs(n+1, check+[num[n]])
    dfs(n+1, check)

N, S = map(int, input().split())
num = list(map(int, input().split()))
visited =  [0]*N
ans = 0

dfs(0, [])

print(ans)