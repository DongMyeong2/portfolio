N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 방향 설정
dir = [ [0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1] ]

# 초기 구름 위치
cloud = [ [N-1,0], [N-1,1], [N-2,0], [N-2,1] ]

# 시뮬레이션 시작
for _ in range(M):
    d, s = map(int, input().split())
    dx, dy = dir[d-1]

    # 구름 이동
    new_cloud = []
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx * s) % N
        cloud[i][1] = (cloud[i][1] + dy * s) % N
        matrix[cloud[i][0]][cloud[i][1]] += 1
        new_cloud.append((cloud[i][0], cloud[i][1]))

    # 물복사 버그
    cloud_set = set(new_cloud)  # 집합 사용으로 탐색 시간 절약
    check = []
    for x, y in new_cloud:
        sm = 0
        for j in range(1, 8, 2):  # 대각선 탐색
            Dx = x + dir[j][0]
            Dy = y + dir[j][1]
            if 0 <= Dx < N and 0 <= Dy < N and matrix[Dx][Dy] > 0:
                sm += 1
        check.append(sm)

    for i, (x, y) in enumerate(new_cloud):
        matrix[x][y] += check[i]

    # 새로운 구름 생성
    cloud = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (i, j) not in cloud_set:
                matrix[i][j] -= 2
                cloud.append([i, j])

# 최종 결과 계산
result = sum(sum(row) for row in matrix)
print(result)