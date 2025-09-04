
# case 2
T = 10

for test_case in range(1, T + 1):
    dmp = int(input())
    nums = list(map(int, input().split()))

    for x in range(dmp):
        nums.sort()
        nums[0] += 1
        nums[-1] -= 1
    print(f"#{test_case} {max(nums)-min(nums)}")
