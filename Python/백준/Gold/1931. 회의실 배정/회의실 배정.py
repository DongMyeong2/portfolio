N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

now_s, now_e = lst[0][0], lst[0][1]
ans = 1

for i in range(1, N):
    check_s, check_e = lst[i][0], lst[i][1]
    if check_s >= now_e:
        now_s, now_e = check_s, check_e
        ans += 1
    elif check_e < now_e:
        now_s, now_e = check_s, check_e
        
print(ans)