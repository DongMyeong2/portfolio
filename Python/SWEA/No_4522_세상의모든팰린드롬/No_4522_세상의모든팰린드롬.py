
# TIP : '?'는 반대쪽 같은 위치의 문자와 바꿈

T = int(input())

for test_case in range(1, T + 1):
    word = list(input())

    for i in range(len(word)):
        if word[i] == '?':
            word[i] = word[len(word) - (1+i)]

    if word == word[-1::-1]:
        print("#"+str(test_case), "Exist")
    else:
        print("#"+str(test_case), "Not exist")
