
T = int(input())

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    if A != B:
        if A + B <= N:
            MAX = min(A, B)
            MIN = 0
        elif A + B > N:
            MAX = min(A,B)
            MIN = A + B - N
    else:
        if A + B <= N:
            MAX = A
            MIN = 0
        elif A + B > N:
            MAX = A
            MIN = A + B - N
    print("#"+str(test_case), MAX, MIN)
