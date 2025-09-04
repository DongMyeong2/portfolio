
T = int(input())

for test_case in range(1, T + 1):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    word = list(input())
    result = 0
    for i in range(len(word)):
        if word[i] != alpha[i]:
            break
        result += 1
    print("#"+str(test_case), result)
