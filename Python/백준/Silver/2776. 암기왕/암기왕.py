T = int(input())

for _ in range(T):
    N = int(input())
    N_num = set(map(int, input().split()))  # 리스트를 set으로 변환하여 빠르게 탐색
    M = int(input())
    M_num = list(map(int, input().split()))

    result = []
    for m in M_num:
        if m in N_num:
            result.append(1)
        else:
            result.append(0)

    print("\n".join(map(str, result)))