
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N_check = 1
    ans = -1

    while True:
        if N_check ** 3 == N:
            ans = N_check
            break
        if N_check ** 3 > N:
            break
        N_check += 1

    print("#"+str(test_case), ans)
