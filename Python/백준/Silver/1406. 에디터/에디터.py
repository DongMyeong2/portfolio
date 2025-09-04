import sys
input_data = sys.stdin.read().splitlines()
# 첫 줄은 초기 문자열, 두번째 줄은 명령어 개수, 그 이후가 명령어들입니다.
left_stack = list(input_data[0])
right_stack = []
# 첫 번째 줄은 인덱스 0, 두 번째 줄은 인덱스 1, 명령어들은 2부터 시작합니다.
for cmd in input_data[2:]:
    # 각 명령어는 공백으로 구분되어 있습니다.
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P':
        # 명령어는 "P x" 형태이므로, 2번째 문자가 추가할 문자입니다.
        left_stack.append(cmd[2])
        
sys.stdout.write("".join(left_stack + right_stack[::-1]))