
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    word.sort()
    word_set = list(set(word))
    for i in range(len(word_set)):
        for _ in range((word.count(word_set[i])//2)*2):
            word.remove(word_set[i])
    if bool(word):
        print("#"+str(test_case), "".join(word))
    else:
        print("#"+str(test_case), "Good")
