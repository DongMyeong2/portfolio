T = int(input())
    # P : A회사 1리터당 가격
    # Q : B회사 R리터 이하 기본 요금
    # R : B회사 기본 요금 한계
    # S : B회사 1리터당 가격
    # W : 사용량
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P*W
    if W <= R:
        B = Q
    else:
        B = Q + ((W-R)*S)
        
    if A <= B:
        print("#"+str(test_case), A)
    elif A > B:
        print("#"+str(test_case), B)