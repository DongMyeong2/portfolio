import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    word = input().strip()
    left = []
    right = []

    for w in word:
        if w == '<':
            if left:
                right.append(left.pop())
        elif w == '>':
            if right:
                left.append(right.pop())
        elif w == '-':
            if left:
                left.pop()
        else:
            left.append(w)
    
    print(''.join(left + right[::-1]))
