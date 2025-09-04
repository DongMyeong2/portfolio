while True:
    word = input()
    if word == '.':
        break
    check = True
    stack = []
    for x in word:
        if (x == '(') or (x == '['):
            stack.append(x)
        elif x == ')':
            if len(stack) == 0 or stack.pop() != '(':
                check = False
                break
        elif x == ']':
            if len(stack) == 0 or stack.pop() != '[':
                check = False
                break

    if not check or len(stack) > 0:
        print('no')
    else:
        print('yes')