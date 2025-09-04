
def is_safe(row, col, queens):
    # queens는 각 행에서 퀸이 놓여진 열 정보를 담고 있는 리스트
    for r in range(row):
        c = queens[r]
        # 같은 열에 있거나, 대각선에 위치하는지 확인
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_n_queens(n, row, queens):
    if row == n:
        # 모든 행에 퀸을 성공적으로 놓은 경우
        return 1  
    count = 0
    for col in range(n):
        if is_safe(row, col, queens):
            queens[row] = col  # 퀸을 (row, col)에 놓음
            count += solve_n_queens(n, row + 1, queens)
    return count

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    queens = [-1] * N  # 각 행에 퀸이 놓인 열을 기록 (-1은 아직 놓이지 않음을 의미)
    result = solve_n_queens(N, 0, queens)  # 0번째 행부터 시작
    print(f"#{test_case} {result}")
