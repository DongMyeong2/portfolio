
T = int(input())

for test_case in range(1, T + 1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    result = []
    word = list(input())
    for i in range(len(word)):
        if word[i] not in vowel:
            result.append(word[i])
    print("#"+str(test_case), "".join(result))
