
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    password = list(map(int, input().split()))
    command_count = int(input())
    command = list(input().split())

    index = 0
    for _ in range(command_count):
        if command[index] == "I":
            for i in range(int(command[index+2])):
                password.insert(int(command[index+1]), command[ index + 2 + int(command[index+2]) - i])
            index += 3 + int(command[index+2])
        elif command[index] == "D":
            for _ in range(int(command[index+2])):
                password.pop(int(command[index+1]))
            index += 3
    print("#"+str(test_case), " ".join(map(str, password[:10])))
