word = input()

stack = []
result = []

for w in word:
    if w == '<':
        if len(stack) != 0:
            result.append(''.join(stack[::-1]))
        stack = []
        stack.append(w)
    elif w == '>':
        stack.append(w)
        result.append(''.join(stack))
        stack = []
    elif w == ' ':
        if '<' in stack:
            stack.append(w)
        else:
            result.append(''.join(stack[::-1]))
            result.append(w)
            stack=[]
    else:
        stack.append(w)

if len(stack) != 0:
    result.append(''.join(stack[::-1]))

print("".join(result))