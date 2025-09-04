
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    center = int(N/2)
    matrix = []
    result = 0
    for _ in range(N):
        matrix.append(list(input()))

    row_down = center
    for i in range(center):
        for _ in range(row_down):
            matrix[i].pop(0)
            matrix[i].pop(-1)
        row_down -= 1

    row_up = 1
    for i in range(center+1, N):
        for _ in range(row_up):
            matrix[i].pop(0)
            matrix[i].pop(-1)
        row_up += 1

    for i in range(N):
        matrix[i] = [int(j) for j in matrix[i]]
        result += sum(matrix[i])

    print("#"+str(test_case), result)
