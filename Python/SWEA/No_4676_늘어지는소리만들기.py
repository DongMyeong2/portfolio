
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    H = int(input())
    place = list(map(int, input().split()))
    place.sort()
    place_set = list(set(place))
    for i in place_set[-1::-1]:
        word.insert(i, "-" * place.count(i))
    print("#"+str(test_case), "".join(word))
