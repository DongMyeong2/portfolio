
# case 2 : 부분집합 이용 안함
T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    result_list = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                result_list.append(nums[i]+nums[j]+nums[k])
    result_list.sort(reverse = True)
    result = list(set(result_list))

    print("#"+str(test_case), result[4])
