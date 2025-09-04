
for test_case in range(1, 11):
    T = int(input())

    password = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            remove = password.pop(0) - i
            password.append(remove)
            if password[7] <= 0: 
                password[7] = 0
                break # for문을 멈추는 break
        if password[7] <= 0:
                password[7] = 0
                break # while문을 멈추는 break
    print("#"+str(T), " ".join(map(str, password)))
