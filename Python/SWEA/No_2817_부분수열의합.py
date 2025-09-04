
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(A[j])
        if sum(subset) == K:
            result.append(subset)
    print("#"+str(test_case), len(result))
