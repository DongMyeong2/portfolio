A, B = map(int, input().split())
B = str(B)
ans = 0
result = True

while True:
    if int(B) < A:
        result = False
        break
    elif int(B) == A:
        break

    if int(B)%2 == 0:
        B = str(int(B) // 2)
        ans += 1
    elif B[-1] == '1':
        B = B[:len(B)-1]
        ans += 1
    else:
        result = False
        break

if result:
    print(ans+1)
else:
    print(-1)