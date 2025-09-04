from copy import deepcopy

def dfs(n, start, array):
    global ans
    if n == 3:  # 벽 3개를 모두 세운 경우
        temp_array = deepcopy(array)  # 배열을 깊은 복사
        result = spread_virus(temp_array)  # 바이러스 퍼뜨리기
        safe_area = sum(row.count(0) for row in result)  # 안전 영역 크기 계산
        ans = max(ans, safe_area)  # 안전 영역 최대값 갱신
        return

    for row in range(N):
        for col in range(M):
            if (row, col) > start and array[row][col] == 0:
                array[row][col] = 1  # 벽을 세움
                dfs(n + 1, (row, col), array)  # 다음 단계 진행
                array[row][col] = 0  # 원상태로 되돌림

def spread_virus(check):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = []

    for x in range(N):
        for y in range(M):
            if check[x][y] == 2:  # 바이러스 위치를 큐에 추가
                queue.append((x, y))

    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < M) and (check[nx][ny] == 0):  # 빈 칸일 경우
                check[nx][ny] = 2  # 바이러스를 퍼뜨림
                queue.append((nx, ny))

    return check

# 입력
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0, (-1, -1), matrix)  # DFS 시작

# 결과 출력
print(ans)