
# TIP : N을 포함하고 나머지 곱해진 연속된 수가 모두 합성수

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    print("#"+str(test_case), N*9, N*8)
