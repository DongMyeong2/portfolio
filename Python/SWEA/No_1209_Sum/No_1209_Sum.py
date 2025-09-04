
# 행의 합 중 가장 큰 값을 구하는 함수
def matrix_row(matrix):
    SUM = []
    for i in range(100):
        SUM.append(sum(matrix[i]))
    return max(SUM)
# 대각 요소의 합을 구하는 함수
def matrox_diagonal(matrix):
    SUM = []
    for i in range(100):
        SUM.append(matrix[i][i])
    return sum(SUM)

for test_case in range(10):
    T = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    matrix_reverse = []
    for i in range(100):
        matrix_reverse.append(matrix[i][-1::-1])

    matrix_trans = [list(row) for row in zip(*matrix)]

    print("#"+str(T), max(matrix_row(matrix), matrix_row(matrix_trans), matrox_diagonal(matrix), matrox_diagonal(matrix_reverse)))
