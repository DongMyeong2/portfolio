K = int(input())
N = []

for _ in range(K):
  num=int(input())
  if num == 0:
    N.pop(-1)
  else:
    N.append(num)

print(sum(N))