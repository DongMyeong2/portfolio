import sys
from collections import deque

N = int(input())
que = deque([])
result = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if que:
            result.append(que.popleft())
        else:
            result.append('-1')
    elif cmd[0] == 'size':
        result.append(len(que))
    elif cmd[0] == 'empty':
        if que:
            result.append(0)
        else:
            result.append(1)
    elif cmd[0] == 'front':
        if que:
            result.append(que[0])
        else:
            result.append('-1')
    elif cmd[0] == 'back':
        if que:
            result.append(que[-1])
        else:
            result.append('-1')

sys.stdout.write('\n'.join(map(str, result)))