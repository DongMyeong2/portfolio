
# case 1
T = 10

for test_case in range(1, T + 1):
    count = int(input())
    height = list(map(int, input().split()))
    for _ in range(count):
        height[height.index(max(height))] -= 1
        height[height.index(min(height))] += 1
        top = height[height.index(max(height))]
        bottom = height[height.index(min(height))]
    print("#"+str(test_case), top-bottom)
