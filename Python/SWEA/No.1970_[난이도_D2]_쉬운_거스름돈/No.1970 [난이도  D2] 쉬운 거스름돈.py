T = int(input())

for test_case in range(1, T + 1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    N = int(input())
    for i in range(8):
        N, money[i] = N%money[i] , N//money[i]
    print("#"+str(test_case))
    print(" ".join(map(str, money)))