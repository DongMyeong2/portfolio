
# TIP : 방향 정해서 탐색하는 것까지 구현했으니
#       뒤집을 반대 색상을 기억(저장) 해뒀다가 탐색 방향에
#       같은 색상 있으면 뒤집고, 없으면 뒤집지 않는 부분 구현 못함

# 방향 탐색 (8방향: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 돌을 놓는 함수
def place_stone(dp, row, col, stone, N):
    # 현재 놓은 돌의 반대 색상
    opposite = 2 if stone == 1 else 1

    # 8방향으로 돌을 확인
    for dx, dy in directions:
        r, c = row + dx, col + dy
        # 범위를 벗어 났으므로 다른 방향으로 조사
        if r < 1 or r > N or c < 1 or c > N:
            continue
        if dp[r][c] == opposite:  # 인접한 돌이 상대방의 돌이면
            flip_positions = [(r, c)]
            while True:
                r += dx
                c += dy
                if r < 1 or r > N or c < 1 or c > N or dp[r][c] == 0:
                    break
                if dp[r][c] == stone:  # 자신의 돌을 만나면 돌을 뒤집음
                    for flip_r, flip_c in flip_positions:
                        dp[flip_r][flip_c] = stone
                    break
                flip_positions.append((r, c))

# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, T+1):
    # N: 보드 크기, M: 돌을 놓는 횟수
    N, M = map(int, input().split())

    # 보드 초기화 (0으로 초기화하고, 인덱스를 1부터 사용하기 위해 N+2 크기로 만듦)
    dp = [[0] * (N+2) for _ in range(N+2)]

    # 초기 돌 배치 (가운데에 4개의 돌을 배치)
    dp[N//2][N//2] = dp[N//2+1][N//2+1] = 2  # 백돌
    dp[N//2][N//2+1] = dp[N//2+1][N//2] = 1  # 흑돌

    # M번의 돌 놓기
    for _ in range(M):
        col, row, stone = map(int, input().split())
        dp[row][col] = stone  # 해당 위치에 돌을 놓음
        place_stone(dp, row, col, stone, N)  # 돌을 놓고 뒤집기 처리

    # 흑돌(1)과 백돌(2)의 개수를 세기
    black_count = sum(row.count(1) for row in dp)
    white_count = sum(row.count(2) for row in dp)

    # 결과 출력
    print(f"#{test_case} {black_count} {white_count}")
