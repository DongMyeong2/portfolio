# 3x3 행렬 검사
def matrix_small(matrix, row, col,num): 
    result = []
    for i in range(3):
        for j in range(3):
            result.append(matrix[row + i][col + j])
    result.sort()
    if result == num:
        return 1
    else:
        return 0

# 행과 열 검사
def matrix_line(matrix, row, num):
    result = matrix[row]
    result.sort()
    if result == num:
        return 1
    else:
        return 0
    
T = int(input())

for test_case in range(1, T + 1):
    matrix =[]
    correct = [1]*9
    result_small = []
    result_row = []
    result_col = []
    num = [1,2,3,4,5,6,7,8,9]
    for _ in range(9):
        matrix.append(list(map(int, input().split())))
    matrix_reverse = [list(row) for row in zip(*matrix)]
    
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            result_small.append(matrix_small(matrix, i, j, num))
    for i in range(9):
        result_row.append(matrix_line(matrix, i, num))
        result_col.append(matrix_line(matrix_reverse, i, num))
    if result_small == correct and result_row == correct and result_col == correct:
        print("#"+str(test_case), 1)
    else:
        print("#"+str(test_case), 0)