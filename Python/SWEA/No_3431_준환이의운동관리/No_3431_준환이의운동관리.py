
T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
        print("#"+str(test_case), L-X)
    elif X >= L and X <= U:
        print("#"+str(test_case), 0)
    elif X > U:
        print("#"+str(test_case), -1)
