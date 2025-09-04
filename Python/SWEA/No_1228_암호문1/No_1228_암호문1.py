
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    password = list(map(int, input().split()))
    command_count = int(input())
    command = list(input().split())

    index = 0
    count = 1
    while count <= command_count:
        count+=1
        for i in range(int(command[index+2])):
            password.insert(int(command[index+1]), int(command[ index + 2 + int(command[index+2]) - i ]))
        index += 3 + int(command[index+2])
    print("#"+str(test_case), " ".join(map(str, password[0:10])))
