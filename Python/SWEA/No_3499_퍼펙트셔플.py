
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    result = []
    if len(card) % 2 ==0:
        half = len(card)//2
        card1 = card[:half]
        card2 = card[half:]
        for i in range(half):
            result.append(card1[i])
            result.append(card2[i])
    else:
        half = len(card)//2
        card1 = card[:half+1]
        card2 = card[half+1:]
        for i in range(half):
            result.append(card1[i])
            result.append(card2[i])
        result.append(card1[-1])

    print("#"+str(test_case), " ".join(result))
