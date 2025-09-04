def spin(matrix):
    matrix_reverse =[]
    matrix_reverse = [list(row) for row in zip(*matrix)]
    for i in range(len(matrix_reverse)):
        matrix_reverse[i] = matrix_reverse[i][-1::-1]
    return matrix_reverse

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = []
    for i in range(N):
        num = list(map(str, input().split()))
        result.append(num)
    
    result_90 = spin(result)
    result_180 = spin(result_90)
    result_270 = spin(result_180)
    
    print("#"+str(test_case))
    for i in range(N):
        print("".join(result_90[i]), "".join(result_180[i]), "".join(result_270[i]))