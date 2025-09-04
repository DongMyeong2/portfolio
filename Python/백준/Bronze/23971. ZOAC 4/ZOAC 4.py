H, W, N, M = map(int, input().split())

num_W = 1
num_H = 1

count_W = 0
count_H = 0

while num_W <= W:
  count_W+=1
  num_W += M+1

while num_H <= H:
  count_H+=1
  num_H += N+1
  
print(count_W*count_H)