
T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    result = [ 0 for _ in range(N)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            result[j] = i
    print("#"+str(test_case), " ".join(map(str, result)))
