def bfs():
    queue = ([(0, 0, 1)])  # 시작 좌표와 경로 길이 (1부터 시작)
    visited[0][0] = True  # 시작 위치 방문 표시

    while queue:
        x, y, dist = queue.pop(0)
        if x == N - 1 and y == M - 1:
            return dist
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 방문 여부 배열
visited = [[False] * M for _ in range(N)]

print(bfs())