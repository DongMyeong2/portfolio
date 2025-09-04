
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = []
    for _ in range(N):
        result.append("1/"+str(N))
    print("#"+str(test_case), " ".join(result))
