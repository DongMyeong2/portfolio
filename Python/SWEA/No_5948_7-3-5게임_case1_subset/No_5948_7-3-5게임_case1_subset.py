
# case 1 : 부분집합 이용
T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    n = len(nums)
    result_list = []

    # 모든 가능한 2^n 개의 부분집합을 탐색
    for i in range(1 << n):  # 2^n == 1 << n
        subset = []
        for j in range(n):
            if i & (1 << j):  # i의 j번째 비트가 1인지 확인
                subset.append(nums[j])
        if len(subset) == 3:
            result_list.append(subset)

    for i in range(len(result_list)):
        result_list[i] = sum(result_list[i])

    result_list.sort(reverse = True)
    result = list(set(result_list))

    print("#"+str(test_case), result[4])
