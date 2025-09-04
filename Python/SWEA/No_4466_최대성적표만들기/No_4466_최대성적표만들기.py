
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    result = 0
    for _ in range(K):
        result+=score.pop(-1)
    print("#"+str(test_case), result)
