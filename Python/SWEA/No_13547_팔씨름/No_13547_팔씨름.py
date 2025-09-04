
T = int(input())

for test_case in range(1, T + 1):
    result = list(input())
    if result.count('x') <= 7:
        print("#"+str(test_case), "YES")
    else:
        print("#"+str(test_case), "NO")
