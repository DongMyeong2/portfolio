
# case 3 : 비트마스크 -> 시간 초과

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 10**9 - 1

    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == K:
            check = max(subset) - min(subset)
            ans = min(ans, check)
    print("#" + str(test_case), ans)
