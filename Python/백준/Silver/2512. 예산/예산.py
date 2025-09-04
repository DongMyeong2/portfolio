N = int(input())
num = list(map(int, input().split()))
M = int(input())

if sum(num) <= M:
    M = sum(num)

left, right = 0, M
result = 0

while left <= right:
    mid = (left+right)//2
    if mid > max(num):
        mid = max(num)
    check = 0

    for test in num:
        if test < mid:
            check += test
        else:
            check += mid

    if check > M:
        right = mid - 1
    elif check == M:
        result = mid
        break
    else:
        result = max(result, mid)
        left = mid + 1

print(result)