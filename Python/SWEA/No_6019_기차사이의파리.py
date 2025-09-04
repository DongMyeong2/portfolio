
T = int(input())

for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D / (A+B) # 기차가 충돌하기까지 걸린 시간
    print("#"+str(test_case), time*F)
