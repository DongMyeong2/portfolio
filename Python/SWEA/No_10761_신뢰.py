
for t in range(int(input())):
    a = list(input().split())
    n = int(a[0])
    ans = {'O' : [1,0], 'B' : [1,0]}
    cnt = 0
    for i in range(1, n*2, 2):
        x = a[i]
        b = int(a[i+1])
        k = abs(b - ans[x][0])
        time = cnt - ans[x][1]
        if k <= time:
            cnt += 1
        else:
            cnt += k - time + 1
        ans[x] = [b,cnt]
    print(f'#{t+1} {cnt}')
