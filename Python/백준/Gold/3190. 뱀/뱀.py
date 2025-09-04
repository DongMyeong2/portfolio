N = int(input())
K = int(input())

matrix = []
for _ in range(N+2):
  matrix.append([0]*(N+2))

for _ in range(K):
  r,c = map(int, input().split())
  matrix[r][c] = 1

S = int(input())
S_info = {}
for _ in range(S):
  X, C = input().split()
  S_info[int(X)] = C

spin = [ [1,0], [0,-1], [-1,0], [0,1] ]
dic = [0,1]
snake = [ [1,1] ]
ans = 0

while snake[-1][0] >= 1 and snake[-1][0] <= N and snake[-1][1] >= 1 and snake[-1][1] <= N:
  ans += 1
  dx, dy = dic[0], dic[1]
  if [snake[-1][0]+dx, snake[-1][1] + dy] in snake:
    break
  
  snake.append( [snake[-1][0]+dx, snake[-1][1] + dy] )

  if matrix[snake[-1][0]][snake[-1][1]] == 1:
    matrix[snake[-1][0]][snake[-1][1]] = 0
  else:
    snake.pop(0)

  if ans in S_info.keys():
    if S_info[ans] == 'D':
      dic = spin[ (spin.index(dic) + 1) % 4 ]
    elif S_info[ans] == 'L':
      dic = spin[ (spin.index(dic) + -1) % 4 ]

print(ans)