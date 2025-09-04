
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N_box = 0 # 1사분면 위의 조건 만족하는 점의 갯수
    for x in range(1, N+1):
        for y in range(1, N+1):
            if (x**2)+(y**2) <= N**2:
                N_box+=1

    # 각 사분면 위의 조건 만족하는 점의 갯수 + x축,y축 위의 조건 만족하는 점의 갯수 + 원점
    count = (N_box + N)*4 +1 

    print("#"+str(test_case), count)
