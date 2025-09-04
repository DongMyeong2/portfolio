N, M = map(int, input().split())

arr = [ list(input()) for _ in range(N) ]

result = 64

for row in range(N-8+1):
    for col in range(M-8+1):
        check = [ arr[row+r][col:col+8] for r in range(8) ]
        color = ['B', 'W']
        for start in color:
            count = 0
            for r in range(8):
                for c in range(8):
                    if (r + c) % 2 == 0:
                        if start != check[r][c]:
                            count += 1
                    else:
                        if start == check[r][c]:
                            count += 1
            result = min(result, count)
print(result)