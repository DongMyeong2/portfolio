
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    for i in range(len(word)):
        if word[i] == 'b':
            word[i] = 'd'
        elif word[i] == 'd':
            word[i] = 'b'
        elif word[i] == 'p':
            word[i] = 'q'
        elif word[i] == 'q':
            word[i] = 'p'
    print("#"+str(test_case), "".join(word[-1::-1]))
