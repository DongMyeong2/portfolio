T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = []
    word = []
    for i in range(N):
        word.append(list(map(str, input().split())))

    for j in range(N):
        result += list(word[j][0] * int(word[j][1]))

    print("#" + str(test_case))
    for k in range(0, len(result), 10):  # 인덱스 0을 시작으로 result 길이의 전 까지, 10씩
        print("".join(result[k:k + 10]))