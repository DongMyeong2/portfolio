
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    P = list(map(int, input().split()))
    result = []
    while len(result) != N:
        for i in range(1, len(P)):
            if (P[0]//3) * 4 == P[i]:
                result.append(P[0])
                P.pop(i)
                P.pop(0)
                break
    print("#"+str(test_case), " ".join(map(str, result)))
