from collections import deque

N = int(input())
dic = {}

for i in range(N):
    dic[i] = deque(input().split())

word = list(input().split())

possible = True
for w in word:
    found = False
    for i in range(N):
        if dic[i] and dic[i][0] == w:
            dic[i].popleft()
            found = True
            break  # 한 단어는 한 앵무새에게만서 나와야 하므로 break
    if not found:
        possible = False
        break

# 모든 앵무새가 할 말을 다 했는지 확인
for i in range(N):
    if dic[i]:  # 남은 단어가 있다면 실패
        possible = False
        break

print('Possible' if possible else 'Impossible')