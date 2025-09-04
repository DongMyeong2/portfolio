
# TIP : 리스트의 각 원소가 가장 큰 경우일 때를 생각하자

def subsequence(arr, n):
    # DP 배열 초기화: 각 위치에서 최소 부분 수열의 길이는 1
    dp = [1] * n

    # 각 원소가 가장 큰 값일 때 부분 수열의 길이 구하기
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # dp 배열에서 최댓값이 최장 증가 부분 수열의 길이
    return max(dp)

# 입력 처리 및 출력
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = subsequence(arr, N)
    print(f"#{test_case} {result}")
