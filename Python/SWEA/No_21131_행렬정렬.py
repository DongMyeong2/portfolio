
# TIP : 첫 번째 행만 정렬되면 아래도 모두 정렬된 것
#       첫 번째 행렬의 끝에서부터 검사

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    result = []
    count = 0

    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 첫 번째의 순서에 맞는 값이 없으면 False, 있으면 True
    for i in range(1, N):
        if i+1 != matrix[0][i]:
            result.append(False)
        else:
            result.append(True)

    # 행의 끝에서부터 False이면 부분행렬을 전치하고, count 값을 1 증가        
    for i in range(len(result) - 1, -1, -1):
        if not result[i]:
            result[i] = True
            count+=1
            for j in range(i):
                if result[j]:
                    result[j] = False
                else:
                    result[j] = True

    print(count)
