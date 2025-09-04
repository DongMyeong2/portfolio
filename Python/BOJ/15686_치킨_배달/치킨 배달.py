N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

house = []
store = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            store.append([i,j])
        elif matrix[i][j] == 1:
            house.append([i,j])

n = len(store)
case = []

for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(store[j])
    if len(subset) == M:
        case.append(subset)

result = ( (N-1) * 2 ) * len(house)

for CASE in case:
    check = 0
    for HOUSE in house:
        total = (N-1) * 2
        for small_CASE in CASE:
            total = min(total, abs(HOUSE[0] - small_CASE[0]) + abs(HOUSE[1] - small_CASE[1]))
        check += total
    result=min(result, check)
    
print(result)