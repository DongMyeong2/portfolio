def cal (S, L):
    s_sm = l_sm = 0
    for i in range(M):
        for j in range(M):
            s_sm += matrix[S[i]][S[j]]
            l_sm += matrix[L[i]][L[j]]
    return abs(s_sm - l_sm)

def dfs (n, S, L):
    global ans
    if n == N:
        if len(S) == len(L):
            ans = min(ans, cal(S,L))
        return

    dfs(n+1, S+[n], L)
    dfs(n+1, S, L+[n])

N = int(input())
M = N//2
ans = 100 * M * M

matrix = [ list(map(int, input().split())) for _ in range(N) ]

dfs(0, [], [])

print(ans)