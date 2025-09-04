
T = int(input())

for test_case in range(1, T + 1):
    H, W =map(int, input().split())
    matrix = []
    dir = ['^', 'v', '>', '<']

    for _ in range(H):
        matrix.append(list(input()))

    num = int(input())
    command = list(input())

    # 처음 전차의 위치 찾아서 전차의 방향, 위치 반환
    for i in range(H):
        for x in dir:
            if x in matrix[i]:
                now_dir = x
                now_row = i
                now_col = matrix[i].index(x)
                break

    # 입력에 따른 전차의 동작            
    for command in command:
        if command == 'S':
            if now_dir == '<':
                for i in range(now_col, -1, -1):
                    if matrix[now_row][i] == "#":
                        break
                    elif matrix[now_row][i] == "*":
                        matrix[now_row][i] = "."
                        break
            elif now_dir == '>':
                for i in range(now_col, W):
                    if matrix[now_row][i] == "#":
                        break
                    elif matrix[now_row][i] == "*":
                        matrix[now_row][i] = "."
                        break
            elif now_dir == 'v':
                for i in range(now_row, H):
                    if matrix[i][now_col] == "#":
                        break
                    elif matrix[i][now_col] == "*":
                        matrix[i][now_col] = "."
                        break
            elif now_dir == '^':
                for i in range(now_row, -1, -1):
                    if matrix[i][now_col] == "#":
                        break
                    elif matrix[i][now_col] == "*":
                        matrix[i][now_col] = "."
                        break
        elif command == "U":
            now_dir = '^'
            matrix[now_row][now_col] = now_dir
            if now_row >0:
                if matrix[now_row-1][now_col] == '.':
                    matrix[now_row][now_col] = '.'
                    matrix[now_row-1][now_col] = now_dir
                    now_row -= 1
        elif command == "D":
            now_dir = 'v'
            matrix[now_row][now_col] = now_dir
            if now_row < H-1 :
                if matrix[now_row+1][now_col] == '.':
                    matrix[now_row][now_col] = '.'
                    matrix[now_row+1][now_col] = now_dir
                    now_row += 1
        elif command == "R":
            now_dir = '>'
            matrix[now_row][now_col] = now_dir
            if now_col < W -1:
                if matrix[now_row][now_col+1] == '.':
                    matrix[now_row][now_col] = '.'
                    matrix[now_row][now_col+1] = now_dir
                    now_col += 1
        elif command == "L":
            now_dir = '<'
            matrix[now_row][now_col] = now_dir
            if now_col > 0:
                if matrix[now_row][now_col-1] == '.':
                    matrix[now_row][now_col] = '.'
                    matrix[now_row][now_col-1] = now_dir
                    now_col -= 1

    print("#"+str(test_case), end=" ")
    for i in range(H):
        print("".join(matrix[i]))
