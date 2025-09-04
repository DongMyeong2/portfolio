
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    sub = list(int(x) for x in input().split())
    N_index = [x for x in range(1, N+1)]
    for i in range(K):
        N_index.remove(sub[i])
    print("#"+str(test_case), " ".join(map(str, N_index)))
