import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
N = int(input())

que = deque()

while True:
    now = input().strip()
    if now == '-1':
        break
    elif now == '0':
        if que:
            que.popleft()
    else:
        if len(que) < N:
            que.append(now)

if que:
    print(' '.join(que))
else:
    print('empty')