N = int(input())
computer = [ [] for _ in range(N+1) ]
for _ in range(int(input())):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

que = computer[1]
result = []
while que:
    now = que.pop(0)
    if now not in result:
        result.append(now)
    for n in computer[now]:
        if (n not in que) and (n not in result):
            que.append(n)
if 1 in result:
    result.remove(1)
print(len(result))