import sys
input = sys.stdin.read

# 모든 입력을 한 번에 읽고 줄 단위로 분리
data = input().splitlines()
N = int(data[0])
stack = []
result = []

for i in range(1, N + 1):
    cmd = data[i].split()
    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        result.append(stack.pop() if stack else -1)
    elif cmd[0] == '3':
        result.append(len(stack))
    elif cmd[0] == '4':
        result.append(0 if stack else 1)
    elif cmd[0] == '5':
        result.append(stack[-1] if stack else -1)

# 결과 출력도 한 번에
sys.stdout.write('\n'.join(map(str, result)))