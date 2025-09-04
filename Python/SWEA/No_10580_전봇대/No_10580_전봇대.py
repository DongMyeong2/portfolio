
# TIP : 비교하는 전봇대의 줄보다 A전봇대 줄이 더 위에 있으면 B전봇대의 줄은 더 아래로,
#       A전봇대의 줄이 더 아래에 있으면 B전봇대의 줄이 더 위에 위치하면 교차한다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tower = []
    count = 0

    for _ in range(N):
        tower.append(list(map(int, input().split())))

    for i in range(N-1):
        for j in range(i+1, N):
            if tower[i][0] > tower[j][0] and tower[i][1] < tower[j][1]:
                count+=1
            elif tower[i][0] < tower[j][0] and tower[i][1] > tower[j][1]:
                count+=1

    print("#"+str(test_case), count)
