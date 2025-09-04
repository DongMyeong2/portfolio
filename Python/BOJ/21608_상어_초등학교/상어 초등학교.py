N = int(input())
matrix = [ list(map(int,input().split())) for _ in range(N*N) ]

seat = [ [0] * N for _ in range(N) ]
seat[1][1] = matrix[0][0]

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

for now in range(1, N*N):
    student = matrix[now][0]
    like = matrix[now][1:]
    where = []
    info = [0, 0]

    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            like_count = 0
            blank_count = 0
            if seat[row][col] == 0:
                for i in range(4):
                    dic_x = row + dx[i]
                    dic_y = col + dy[i]
                    if (dic_x < 0) or (dic_x >= N) or (dic_y < 0) or (dic_y >= N):
                        continue
                    if seat[dic_x][dic_y] in like:
                        like_count += 1
                    elif seat[dic_x][dic_y] == 0:
                        blank_count += 1
            if like_count > info[0]:
                info[0] = like_count
                info[1] = blank_count
                where = [row, col]
            elif like_count == info[0] and blank_count > info[1]:
                info[1] = blank_count
                where = [row, col]
            elif like_count == info[0] and blank_count == info[1]:
                where = [row, col]

    if info == [0, 0]:
        where = []

    if where:
        seat[where[0]][where[1]] = student
    else:
        for j in range(N):
            if 0 in seat[j]:
                seat[j][seat[j].index(0)] = student
                break

for row in range(N):
    for col in range(N):
        for i in range(N*N):
            if seat[row][col] == matrix[i][0]:
                check = matrix[i][1:]
                check_count = 0
                for j in range(4):
                    dic_x = row + dx[j]
                    dic_y = col + dy[j]
                    if (dic_x < 0) or (dic_x >= N) or (dic_y < 0) or (dic_y >= N):
                        continue
                    if seat[dic_x][dic_y] in check:
                        check_count += 1
                if check_count > 0:
                    ans += 10**(check_count-1)
print(ans)