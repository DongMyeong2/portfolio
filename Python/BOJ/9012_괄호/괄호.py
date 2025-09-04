def check(word):
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

N = int(input())

for _ in range(N):
    word = input()
    if check(word):
        print('YES')
    else:
        print('NO')
