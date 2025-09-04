N = int(input())

stack = []
result = []

for _ in range(N):
    word = input()
    word = word.split(' ')
    if word[0] == 'push':
        stack.append(int(word[1]))
    elif word[0] == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif word[0] == 'size':
        result.append(len(stack))
    elif word[0] == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    else:
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

for i in result:
    print(i)