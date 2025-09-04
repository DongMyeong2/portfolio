
T = int(input())

for test_case in range(1, T + 1):
    dir = list(input())
    a = 1
    b = 1

    for i in range(len(dir)):
        if dir[i] == 'L':
            b += a
        elif dir[i] == 'R':
            a += b
    print("#"+str(test_case), a,b)
