
T = int(input())

for test_case in range(1, T + 1):
    a,b,c = map(int, input().split())
    left = b-a
    right = c-b
    ans = 0.0
    if left != right:
        ans = abs(left - right)/2
    print("#"+str(test_case), ans)
