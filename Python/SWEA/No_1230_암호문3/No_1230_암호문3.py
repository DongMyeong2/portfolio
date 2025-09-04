
# TIP : while문으로 M번만큼만 반복하도록 했는데
#       for문을 사용하여 command 리스트 전체를 반복하여 답을 찾아도 됨

T = 10

for test_case in range(1, T + 1):
    N = int(input()) # 원본 암호문 뭉치 속 암호문의 개수 N
    password = list(map(int, input().split())) # 원본 암호문 뭉치
    M = int(input()) # 명령어의 개수
    command = list(input().split())
    command_count = 0
    command_index = 0
    while command_count <M:
        if command[command_index] == 'I':
            for i in range(int(command[command_index+2])):
                password.insert( int(command[command_index+1]), command[command_index+ 2 + int(command[command_index+2]) - i ])                               
            command_count += 1
            command_index += 3 + int(command[command_index+2])
        elif command[command_index] == 'A':
            for i in range(int(command[command_index+1])):
                password.append(command[command_index+2+i])
            command_count += 1
            command_index += 2+int(command[command_index+1])
        elif command[command_index] == 'D':
            for i in range(int(command[command_index+2])):
                password.pop(int(command[command_index+1]))
            command_count += 1
            command_index += 3

    print("#"+str(test_case), " ".join(password[0:10]))
