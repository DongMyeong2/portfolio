def check_r():
    out = 0
    for i in range(N):
        count = 1
        word = arr[i][0]
        for r in range(1, N):
            if word == arr[i][r]:
                count += 1
            else:
                word = arr[i][r]
                out = max(count, out)
                count = 1
        out = max(count, out)
    return out

def check_c():
    out = 0
    for i in range(N):
        count = 1
        word = arr[0][i]
        for c in range(1, N):
            if word == arr[c][i]:
                count += 1
            else:
                word = arr[c][i]
                out = max(count, out)
                count = 1
        out = max(count, out)
    return out

N = int(input())
arr = [ list(input()) for _ in range(N)]
ans = 0
direction = [ [0,1], [1,0] ]

for row in range(N):
    for col in range(N):
        ans = max(ans, check_r(), check_c())
        for dx, dy in direction:
            x, y = row + dx, col + dy
            if 0 <= x < N and 0 <= y < N and arr[x][y] != arr[row][col]:
                arr[x][y], arr[row][col] = arr[row][col], arr[x][y]
                ans = max(ans, check_r(), check_c())
                arr[row][col], arr[x][y] = arr[x][y], arr[row][col]

print(ans)