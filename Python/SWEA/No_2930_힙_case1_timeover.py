
# case 1 : 내 풀이 -> 시간 초과

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    hip = []
    result = []
    for _ in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            hip.append(cmd[1])
        else:
            if not hip:
                result.append(-1)
            else:
                result.append(hip.pop(hip.index(max(hip))))
    print("#"+str(test_case), " ".join(map(str, result)))
