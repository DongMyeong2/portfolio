
T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A+B >= 24:
        result = A+B -24
        print("#"+str(test_case), result)
    else:
        result = A+B
        print("#"+str(test_case), result)
