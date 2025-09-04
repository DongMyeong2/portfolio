T = int(input())

direction = [ [0,1], [1,0], [0,-1], [-1,0] ]

for _ in range(T):
    N, M, K = map(int, input().split())
    where = [ list(map(int, input().split())) for _ in range(K) ]
    ans = 0

    while where:
        X,Y = where.pop(0)
        check = [[X,Y]]
        while check:
            x,y = check.pop(0)
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if (0<=nx<N) and (0<=ny<M) and ([nx, ny] in where):
                    where.remove([nx,ny])
                    check.append([nx,ny])
        ans += 1

    print(ans)