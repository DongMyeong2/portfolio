
# case 2 : 백트랙킹 -> 시간 초과

def dfs(n, lst):
    global ans
    if n == N:
        if len(lst) == K:
            check = max(lst) - min(lst)
            ans = min(ans, check)
        return

    dfs(n+1, lst)

    lst.append(A[n])
    dfs(n+1, lst)
    lst.pop()

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 10**9 - 1
    dfs(0, [])
    print("#" + str(test_case), ans)
