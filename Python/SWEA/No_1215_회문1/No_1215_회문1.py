
def result(matrix, N):
    count = 0
    for i in range(8):
        for j in range(9-N):
            result = matrix[i][j:j+N]
            if result == result[-1::-1]:
                count+=1
    return count

for test_case in range(1, 11):
    matrix = []

    N = int(input())
    for _ in range(8):
        matrix.append(list(input()))

    matrix_reverse = [list(row) for row in zip(*matrix)]

    print("#"+str(test_case), result(matrix, N)+result(matrix_reverse, N))
