N = int(input())

num = 1
stack = []
result = []
check = True

for _ in range(1, N+1):
    now = int(input())
    while True:
        if num <= now:
            stack.append(num)
            result.append('+')
            num += 1
        else:
            out = stack.pop()
            result.append('-')
            if out != now:
                stop = True
                break
            else:
                stop = False
                break
    if stop:
        check = False
        break

if check:
    for word in result:
        print(word)
else:
    print('NO')