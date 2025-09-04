def bfs():
    visited = [[0] * N for _ in range(N)]
    result = []
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 1 or arr[row][col] == '0':
                continue
            que = [[row, col]]
            sub = []
            while que:
                x,y = que.pop(0)
                if [x,y] not in sub:
                    sub.append([x,y])
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] == '1':
                        if visited[nx][ny] == 0:
                            que.append([nx,ny])
                            visited[nx][ny] = 1
            result.append(len(sub))
    result.sort()
    return [len(result)] + result

N = int(input())
arr = [ list(input()) for _ in range(N) ]

direction = [ (0,1), (1,0), (0,-1), (-1,0) ]

for x in bfs():
    print(x)