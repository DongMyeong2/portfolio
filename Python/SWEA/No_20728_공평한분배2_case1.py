
# case 1 : 오름차순으로 정렬하고 K개씩 묶어서 그 중 큰 값과 작은 값을 비교

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 10**9 - 1
    for num in range(N-K+1):
        check = A[num+K-1] - A[num]
        ans = min(ans, check)
    print("#" + str(test_case), ans)
