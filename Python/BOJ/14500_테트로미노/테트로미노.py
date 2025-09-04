def dfs(x, y, n, check):
    global ans
    if n == 4:
        ans = max(ans, check)
        return

    dic = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in dic:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, n + 1, check + matrix[nx][ny])
            visited[nx][ny] = False

def calculate_shape(x, y):
    shapes = [
        [(0, 0), (0, 1), (0, -1), (-1, 0)],  # ㅗ 모양
        [(0, 0), (0, 1), (0, -1), (1, 0)],   # ㅜ 모양
        [(0, 0), (1, 0), (-1, 0), (0, 1)],   # ㅏ 모양
        [(0, 0), (1, 0), (-1, 0), (0, -1)]   # ㅓ 모양
    ]
    max_sum = 0
    for shape in shapes:
        shape_sum = 0
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                shape_sum += matrix[nx][ny]
            else:
                break
        else:  # break 없이 완료된 경우만 최대값 갱신
            max_sum = max(max_sum, shape_sum)
    return max_sum

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0
visited = [[False] * M for _ in range(N)]

# 모든 좌표에서 DFS와 ㅗ 모양 검사 수행
for row in range(N):
    for col in range(M):
        visited[row][col] = True
        dfs(row, col, 1, matrix[row][col])  # 깊이 1부터 시작
        visited[row][col] = False
        # ㅗ 모양 검사
        ans = max(ans, calculate_shape(row, col))

print(ans)