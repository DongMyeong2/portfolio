
# TIP : 작은 값, 큰 값 모두 비교하는게 아니라 둘 중 한 값만 계산해주면
#       다른 값은 알아서 계산되는 것과 같음

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dump = []
    result = 0

    for _ in range(N):
        dump.append(int(input()))

    ave = sum(dump) // N

    for i in range(N):
        if dump[i] > ave:
            result += dump[i] - ave

    print("#"+str(test_case), result)
