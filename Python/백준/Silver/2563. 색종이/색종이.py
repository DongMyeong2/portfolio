array = [ [0] * 100 for _ in range(100) ]

ans = 0

for _ in range(int(input())):
    X, Y = map(int, input().split())

    for x in range(X, X+10):
        for y in range(Y, Y+10):
            array[x][y] = 1

for row in range(100):
    ans += array[row].count(1)

print(ans)