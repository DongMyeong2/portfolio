# TIP : N과 M 중 더 작은 값으로 만들어진 리스트에 0을 추가하여 두 리스트의 길이를
#       같게 맞춤. N과 M의 차이만큼 더 짧은 쪽 리스트를 한칸씩 이동시키며 연산

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_a = list(map(int, input().split()))
    M_b = list(map(int, input().split()))
    result = []
    if N < M:
        for _ in range(M - N):
            N_a.append(0)
        for j in range(M-N +1):
            N_times_M = []
            for i in range(M):
                N_times_M.append(N_a[i]*M_b[i])
            result.append(sum(N_times_M))
            N_a.insert(0, 0)
            N_a.pop(-1)
    elif N > M:
        for _ in range(N- M):
            M_b.append(0)
        for j in range(N-M +1):
            N_times_M = []
            for i in range(N):
                N_times_M.append(N_a[i]*M_b[i])
            result.append(sum(N_times_M))
            M_b.insert(0, 0)
            M_b.pop(-1)
    print("#"+str(test_case), max(result))