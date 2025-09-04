
# TIP : 결과를 바로 바로 출력하는게 아니라 모아뒀다가 한 번에 출력하는게 더 빠름

T = int(input())

result = []

for test_case in range(T):
    A, B, C, D = map(int, input().split())
    Alice = A / B
    Bob = C / D

    if Alice > Bob:
        result.append("ALICE")
    elif Alice < Bob:
        result.append("BOB")
    else:
        result.append("DRAW")

for i in range(T):
    print("#"+str(i+1), result[i])
