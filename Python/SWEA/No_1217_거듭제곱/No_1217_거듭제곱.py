
for test_case in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    result = 1
    for _ in range(M):
        result *= N
    print("#"+str(T), result)
