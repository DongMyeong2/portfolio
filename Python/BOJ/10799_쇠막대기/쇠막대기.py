word = input()

result = 0
stack = [word[0]]

for idx in range(1, len(word)):
    if word[idx] == ')' and word[idx-1] == '(':
        stack.pop()
        result += len(stack)
    elif word[idx] == '(':
        stack.append('(')
    elif word[idx] == ')':
        stack.pop()
        result += 1

print(result)