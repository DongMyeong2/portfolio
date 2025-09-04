N, K = map(int, input().split())

que = [i for i in range(1, N + 1)]
result = []
now = 0

while len(que) > 1:
    now = (now + K - 1) % len(que)
    result.append(que.pop(now))

result.append(que.pop())
print("<" + ", ".join(map(str, result)) + ">")