n, w, L = map(int, input().split())
que = list(map(int, input().split()))

bridge = [0] * w
result = 0

while True:
    result += 1
    bridge.pop()
    if que:
        if sum(bridge) + que[0] <= L:
            bridge.insert(0, que.pop(0))
        else:
            bridge.insert(0, 0)
    else:
        bridge.insert(0, 0)

    if len(que) == 0 and sum(bridge) == 0:
        break

print(result)