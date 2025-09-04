
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    Income = list(map(int, input().split()))
    Income.sort()

    ave = sum(Income)/N
    count = 0

    for i in range(N):
        if Income[i] <= ave:
            count+=1   
    print("#"+str(test_case), count)
