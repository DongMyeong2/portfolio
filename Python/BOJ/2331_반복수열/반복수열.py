A, P = map(int, input().split())

D = [A]
now = 1

while True:
    cal = 0
    num = str(D[now - 1])
    for n in num:
        cal += int(n)**P
    if cal in D:
        D = D[:D.index(cal)]
        break
    D.append(cal)
    now += 1

print(len(D))