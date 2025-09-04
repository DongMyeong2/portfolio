N, K = map(int, input().split())

value = []
for _ in range(N):
    value.append(int(input()))
value.sort(reverse = True)

result = 0
for coin in value:
    result += K//coin
    K %= coin
    if K == 0:
        break

print(result)