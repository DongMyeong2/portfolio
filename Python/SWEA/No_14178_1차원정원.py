
T = int(input())

for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    sec = D*2 + 1
    if N % sec == 0:
        print("#"+str(test_case), N//sec)
    else:
        print("#"+str(test_case), (N//sec) + 1)
