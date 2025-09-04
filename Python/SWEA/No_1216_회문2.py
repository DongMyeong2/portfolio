
def palindrome(matrix):
    result = []
    for i in range(100): # i : 행 위치
        for j in range(1, 101): # 검사 길이
            for k in range(101 - j): # j 길이의 검사 길이로 k번 반복
                if matrix_reverse[i][k:k+j] == matrix_reverse[i][k:k+j][-1::-1]:
                    result.append(j)
    return max(result)

for test_case in range(1):
    T = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(input()))

    matrix_reverse = [list(row) for row in zip(*matrix)]

    print("#"+str(T), max(palindrome(matrix), palindrome(matrix_reverse)))
