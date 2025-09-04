N = int(input())

W = []
for _ in range(N):
    W.append(int(input()))
W.sort(reverse = True)

ans = W[0]

for i in range(1, N):
    ans = max(ans, W[i]*(i+1))
    
print(ans)