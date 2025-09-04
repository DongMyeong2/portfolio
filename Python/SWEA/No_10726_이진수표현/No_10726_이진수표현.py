
# TIP : 이진수는 2로 나눈 나머지를 비트에 추가하고 나눈 몫을 2로 나누는 과정을 반복
#       몫이 2이 되면 1을 추가하고 멈춤

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    check = [1]*N
    result = []
    # 마지막 N 비트만 확인하면 됨
    for i in range(N):
        # divmao(p, q) -> 출력값 : (p를 q로 나눈 몫, p를 q로 나눈 나머지)
        M, mod = divmod(M,2)[0], divmod(M,2)[1]
        result.insert(0, mod)
    if check == result:
        print("#"+str(test_case), "ON")
    else:
        print("#"+str(test_case), "OFF")
