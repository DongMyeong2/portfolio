
# TIP : 짝수번 울렸을 떄와 홀수번 울렸을 떄 나눠서 생각

T = int(input())

for test_case in range(1, T + 1):
    Input = list(input().split())
    cup = list(Input[0])
    K = int(Input[1])
    if K == 0:
        print("#"+str(test_case), cup.index('o'))
    else:
        if cup[1] == 'o':
            if K%2 == 0:
                print("#"+str(test_case), 1)
            else:
                print("#"+str(test_case), 0)
        else:
            if K%2 == 0:
                print("#"+str(test_case), 0)
            else:
                print("#"+str(test_case), 1)
