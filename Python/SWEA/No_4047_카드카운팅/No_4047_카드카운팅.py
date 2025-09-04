
T = int(input())
for test_case in range(1, T + 1):
    card = input()
    card_type = ['S', 'D', 'H', 'C']
    check = []
    for i in range(0, len(card), 3):
        check.append(card[i:i+3])
    if len(check) != len(set(check)):
        print("#"+str(test_case), "ERROR")
    else:
        print("#"+str(test_case), end = " ")
        for i in card_type:
            print(13 - card.count(i), end=" ")
        print()
