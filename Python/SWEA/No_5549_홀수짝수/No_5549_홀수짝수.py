
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    if num%2 == 0:
        print("#"+str(test_case), "Even")
    elif num%2 != 0:
        print("#"+str(test_case), "Odd")
