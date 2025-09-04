T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    
    for _ in range(N):
        matrix.append([ 1 for _ in range(N)])
        
    for i in range(1, N+1):
        matrix[0][i-1] = str(i)
    
    command = 1 # command -> 1은 아래, 2는 왼, 3은 위, 4는 오른쪽으로 이동
    now = N # 현재 위치의 값
    re = N - 1 # 반복 횟수 ex : N = 5일 때 4개, 3개, 2개, 1개가 두 번씩 반복 4 4 3 3 2 2 1 1
    row = 0 # 현재 행의 위치
    col = N-1 # 현재 열의 위
    
    while now != N*N:
        for i in range(2):
            if command == 1:
                for _ in range(re):
                    matrix[row+1][col]=str(now+1)
                    row += 1
                    now += 1
                command = 2
            elif command == 2:
                for _ in range(re):
                    matrix[row][col-1]=str(now+1)
                    col -= 1
                    now += 1
                command = 3
            elif command == 3:
                for _ in range(re):
                    matrix[row-1][col]=str(now+1)
                    row -= 1
                    now += 1
                command = 4
            elif command == 4:
                for _ in range(re):
                    matrix[row][col+1]=str(now+1)
                    col += 1
                    now += 1
                command = 1
        re -= 1
                
    print("#"+str(test_case))
    for i in range(N):
        print(" ".join(matrix[i]))