T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    que = list(map(int, input().split()))
    count = 0
    while True:
        if len(que) == 1:
            count += 1
            break
        if max(que[1:]) > que[0]:
            que.append(que.pop(0))
            if M == 0:
                M = len(que) - 1
            else:
                M -= 1
        else:
            que.pop(0)
            count += 1
            if M == 0:
                break
            else:
                M -= 1
    print(count)