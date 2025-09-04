
T = int(input())

for test_case in range(1, T + 1):
    a,b,c = map(int, input().split())
    if a == b:
        if a == c:
            print("#"+str(test_case), a)
        elif a != c:
            print("#"+str(test_case), c)
    elif a != b:
        if a == c:
            print("#"+str(test_case), b)
        elif a != c:
            print("#"+str(test_case), a)
