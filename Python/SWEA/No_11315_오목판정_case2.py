
# case 2 : 모든 방향 한번에 확인 

# 방향 탐색에 사용할 델타 값 (오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선)
dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

def check_five_in_a_row(matrix, N):
    # 모든 좌표를 탐색
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 'o':  # 돌이 있는 경우만 탐색
                for direction in range(4):  # 4가지 방향 확인
                    cnt = 1  # 현재 돌 1개 카운트
                    nx, ny = x, y
                    while True:
                        nx += dx[direction]
                        ny += dy[direction]
                        # 범위가 넘어가지 않고, 해당 칸에 돌이 있으면 계속 탐색
                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 'o':
                            cnt += 1
                        else:
                            break
                        if cnt >= 5:  # 돌이 5개 연속인 경우
                            return True
    return False

T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    N = int(input())  # 판의 크기
    matrix = [list(input()) for _ in range(N)]  # N개의 줄로 이루어진 판 입력

    if check_five_in_a_row(matrix, N):
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
