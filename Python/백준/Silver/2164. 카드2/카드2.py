from collections import deque

n = int(input())
que = deque(range(1, n+1))

while len(que) > 1:
    que.popleft()           # 맨 앞 카드 버림
    que.append(que.popleft())  # 다음 카드를 맨 뒤로 이동

print(que[0])