N = int(input())

ans = N
for i in range(N//5, -1, -1):
    if (N-(5*i)) % 2 != 0:
        continue
    ans = min(ans, (N-(5*i))//2 +i)

if ans == N:
    print(-1)
else:
    print(ans)