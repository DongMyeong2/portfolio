def check_matrix(r, c):
    check = [ matrix[r-1][c], matrix[r][c+1], matrix[r+1][c], matrix[r][c-1] ]
    return check

def dfs(row, col, dir):
    global ans
    if matrix[row][col] == 0:
        ans+=1
        matrix[row][col] = -1
    if 0 not in check_matrix(row, col):
        if matrix[row+back[dir][0]][col+back[dir][1]] != 1:
            dfs(row+back[dir][0], col+back[dir][1], dir)
        return
    
    for _ in range(4):
        dir = (dir- 1)%4
        if matrix[row+go[dir][0]][col+go[dir][1]] == 0:
            dfs(row+go[dir][0], col+go[dir][1], dir)
            return
        

N, M = map(int, input().split())
info = list(map(int, input().split()))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

go = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
back = [ [1, 0], [0, -1], [-1, 0], [0, 1] ]

ans = 0
dfs(info[0], info[1], info[2])
print(ans)