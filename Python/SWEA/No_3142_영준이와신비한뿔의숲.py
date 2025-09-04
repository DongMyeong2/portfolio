
# TIP : 연립방정식을 이용

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N : 뿔의 수, M : 동물의수

    for i in range(M+1):
        twin = i #  트윈혼의 수
        uni = M - i # 유니콘의 수
        if twin*2 + uni == N:
            break
    print("#"+str(test_case), uni, twin)
