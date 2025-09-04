N, M = map(int, input().split())
card = list(map(int, input().split()))
ans = 0
for f in range(N):
    for s in range(f+1, N):
        for t in range(s+1, N):
            check = card[f]+card[s]+card[t]
            if check <= M:
                ans = max(ans, check)
print(ans)