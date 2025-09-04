
# TIP : 로직 이해하기

T = int(input())

for test_case in range(1, T + 1):
    p, q = map(float, input().split())

    # s1 : 거꾸로 -> 올바로(한번 뒤집음)
    s1 = (1-p) * q

    # s2 : 올바로 -> 정확하지 않게 -> 거꾸로(한번 뒤집음, 확률 계산x) -> 올바로(두번 뒤집음, 확률 계산x) -> 정확하게(확률 계산x)
    s2 = p * (1-q) * q
    if s1 < s2:
        print("#"+str(test_case), "YES")
    else:
        print("#"+str(test_case), "NO")
