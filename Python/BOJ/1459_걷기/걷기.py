X, Y, W, S = map(int, input().split())

ans = 0

if abs(max(X,Y) - min(X,Y)) % 2 == 0:
    ans += (min(X, Y) * min(W * 2, S)) + (abs(max(X, Y) - min(X, Y)) * min(W, S))
else:
    ans += (min(X, Y) * min(W * 2, S)) + ((abs(max(X, Y) - min(X, Y))-1) * min(W, S) + W)

print(ans)