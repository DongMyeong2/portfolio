# TIP : 입력 받은 문자를 리스트로 저장하고 반복문을 통해 끝에서 부터 리스트를 읽어서
#       다른 리스트에 저장 후 비교

# case 1 : 반복문
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    word_reverse = []
    for i in range(len(word)-1,-1,-1):
        word_reverse.append(word[i])
    
    if word_reverse == word:
        print("#"+str(test_case), 1)
    else:
        print("#"+str(test_case), 0)

# case 2 : 인덱싱
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    word_reverse = word[::-1]
    
    if word_reverse == word:
        print("#"+str(test_case), 1)
    else:
        print("#"+str(test_case), 0)