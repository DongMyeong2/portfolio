T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    matrix_M = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            cal = 0
            for k in range(M):
                cal+=sum(matrix[i+k][j:j+M])
            matrix_M.append(cal)
    print("#"+str(test_case), max(matrix_M))