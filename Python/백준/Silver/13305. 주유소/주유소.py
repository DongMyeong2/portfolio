N = int(input())
road = list(map(int, input().split()))
value = list(map(int, input().split()))

now = value[0]
ans = 0

for i in range(N-1):
    now = min(now, value[i])
    ans += road[i] * now
    
print(ans)