
T = 10

for test_case in range(1, T+1):
    N, str_password = map(str, input().split())
    password = [int(i) for i in list(str_password)]
    index = 0
    while index < len(password)-1:
        if password[index] == password[index+1]:
            for _ in range(2):
                password.pop(index)
            index = 0
        else:
            index += 1
    print("#"+str(test_case), "".join(map(str, password)))
