T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    for i in range(N):
        num[i] = str(num[i])
    print("#"+str(test_case), " ".join(num))