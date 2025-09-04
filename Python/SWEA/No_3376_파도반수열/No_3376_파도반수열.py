
# TIP : 5번째부터 규칙 발생 -> 다음 값 = 바로 전 값 + 바로 전 값의 4번 전 값

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    P = [0,1,1,1,2]
    while True:
        if len(P) > N:
            break
        P.append(P[-1]+P[-5])
    print("#"+str(test_case), P[N])
