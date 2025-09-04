from copy import deepcopy

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0

# 처음에는 전체를 탐색
next_search = [(i, j) for i in range(N) for j in range(N)]

while True:
    copy_country = deepcopy(country)
    check = [[False] * N for _ in range(N)]
    moved = False
    new_search = set()

    # 다음에 탐색할 칸들만 반복
    for row, col in next_search:
        if not check[row][col]:
            team = [(row, col)]
            where = [(row, col)]
            total = country[row][col]
            check[row][col] = True

            # 연합을 찾기 위한 DFS
            while team:
                x, y = team.pop()

                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    if 0 <= dx < N and 0 <= dy < N and not check[dx][dy]:
                        if L <= abs(copy_country[x][y] - copy_country[dx][dy]) <= R:
                            check[dx][dy] = True
                            team.append((dx, dy))
                            where.append((dx, dy))
                            total += copy_country[dx][dy]

            # 연합이 형성되었다면 인구 이동 수행
            if len(where) > 1:
                moved = True
                value = total // len(where)
                for nx, ny in where:
                    country[nx][ny] = value
                    # 인접한 칸을 새로운 탐색 후보에 추가
                    for d in directions:
                        adj_x, adj_y = nx + d[0], ny + d[1]
                        if 0 <= adj_x < N and 0 <= adj_y < N:
                            new_search.add((adj_x, adj_y))

    if not moved:
        break

    # 다음 탐색할 칸을 갱신
    next_search = list(new_search)
    ans += 1

print(ans)
