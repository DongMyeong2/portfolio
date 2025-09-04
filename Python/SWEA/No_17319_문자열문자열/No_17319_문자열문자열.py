
# TIP : 입력값에 대해 하나의 문자열을 2번 반복해서 만들수있느냐 없느냐 판단하는 문제

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    word = input()
    if word[:N//2] == word[N//2:]:
        print("#"+str(test_case), 'Yes')
    else:
        print("#"+str(test_case), 'No')
