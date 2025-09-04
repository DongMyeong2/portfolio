
# TIP : 모든 단어 세트 경우의 수를 부분집합으로 구하기

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    word = [ input() for _ in range(N) ]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # 모든 단어 세트의 경우의 수
    n = len(word)
    result = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(word[j])
        subset="".join(subset)
        result.append(subset)

    # 알파벳이 모두 들어있는 단어 세트의 수 구하기
    count = 0
    for i in range(len(result)):
        check = True
        # 알파벳이 단어 세트에 들어있지 않다면 False로 변경 
        for j in alpha:
            if j not in result[i]:
                check = False
                break
        if check:
            count+=1

    print("#"+str(test_case), count)
