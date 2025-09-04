
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N : 행, M : 열
    number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    matrix = []
    password = []
    for _ in range(N):
        matrix.append(input())

    # 암호가 있는 행 찾기
    for i in range(N):
        if '1' in matrix[i]:
            row = i
            break

    # 암호가 있는 열 찾기
    for i in range(M-6):
        if matrix[row][i:i+7] in number:
            if matrix[row][i+55] == '1': # 마지막 비트의 숫자는 항상 1
                col = i
                break

    # 암호 구하기
    for i in range(0, 56, 7):
        password.append( number.index(matrix[row][col+i:col+i+7]))

    check = (sum(password[0::2])*3) + sum(password[1::2])

    if check % 10 == 0:
        print("#"+str(test_case), sum(password))
    else:
        print("#"+str(test_case), 0)
