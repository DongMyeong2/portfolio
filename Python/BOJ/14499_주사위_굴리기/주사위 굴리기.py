N, M, x, y, K = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

dice = [0] * 6

for i in range(K):
    if cmd[i] == 1:
        y+=1
        if y >= M:
            y-=1
            continue
        dice[2], dice[1], dice[3], dice[5] = dice[3], dice[2], dice[5], dice[1]
    elif cmd[i] == 2:
        y-=1
        if y < 0:
            y+=1
            continue
        dice[2], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[2], dice[3]
    elif cmd[i] == 3:
        x-=1
        if x < 0:
            x+=1
            continue
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif cmd[i] == 4:
        x+=1
        if x >= N:
            x-=1
            continue
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5] ,dice[0]

    where = [x, y]

    if matrix[where[0]][where[1]] == 0:
        matrix[where[0]][where[1]] = dice[2]
    else:
        dice[2] = matrix[where[0]][where[1]]
        matrix[where[0]][where[1]] = 0

    print(dice[5])