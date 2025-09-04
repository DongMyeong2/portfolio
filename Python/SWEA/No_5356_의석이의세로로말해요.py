
T = int(input())

for test_case in range(1, T + 1):
    word = []
    for _ in range(5):
        word.append(list(input()))

    max_length = max([ len(x) for x in word])

    result = []

    # 입력 받은 단어 중 가장 긴 길이의 단어길이만큼 인덱스를 반복하고
    # max_length 보다 짧은 단어의 경우, 인덱스가 더 커질때는 추가 안함 
    for i in range(max_length):
        for j in range(5):
            if len(word[j]) <= i:
                continue
            else:
                result.append(word[j][i])
    print("#"+str(test_case), "".join(result))
