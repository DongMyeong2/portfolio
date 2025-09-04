
T = int(input())

for test_case in range(1, T + 1):
    D, H, M = map(int, input().split())

    meet = (11*24*60) + (11*60) + 11 # 약속 시간
    kick = (D*24*60) + (H*60) + M # 차인걸 깨달은 시간

    if kick < meet:
        print("#"+str(test_case), "-1")
    else:
        print("#"+str(test_case), kick - meet)
