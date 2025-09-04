
# case 1 : 방향 하나씩 확인
def matrix_check(matrix): # 가로, 세로열 확인
    matrix_row = ['o'] * 5
    for i in range(5):
        if matrix[i] == matrix_row:
            return True
    return False

def matrix_diag(matrix): # 아래로 향하는 대각선 확인
    for i in range(5):
        if matrix[i][i] != 'o':
            return False
    return True

def matrix_diag_back(matrix): # 위로 향하는 대각선 확인
    for i in range(4, -1, -1):
        if matrix[4-i][i] != 'o':
            return False
    return True

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))

    matrix_col = [list(row) for row in zip(*matrix)]

    stop = False
    result = False

    # 5x5 행렬로 바꿔서 모두 계산
    for col in range(N - 5 + 1):
        if stop:
            break
        for row in range(N - 5 + 1):
            small_matrix = []
            small_trans_matrix = []
            for i in range(5):
                small_matrix.append(matrix[row+i][col:col+5])
                small_trans_matrix.append(matrix_col[row+i][col:col+5])
            if matrix_check(small_matrix) or matrix_check(small_trans_matrix) or matrix_diag(small_matrix) or matrix_diag_back(small_matrix):
                result = True
                stop = True
                break

    if result:
        print("#"+str(test_case), "YES")
    else:
        print("#"+str(test_case), "NO")
