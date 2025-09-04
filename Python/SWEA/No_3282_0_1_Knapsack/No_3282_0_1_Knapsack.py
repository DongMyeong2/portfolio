
def knapsack(N, K, items):
    # DP 테이블 초기화 (크기 K+1)
    dp = [0] * (K + 1)

    # 각 물건에 대해 DP 테이블 갱신
    for Vi, Ci in items:
        # 역순으로 탐색해야 중복 사용을 막을 수 있음
        for j in range(K, Vi - 1, -1):
            dp[j] = max(dp[j], dp[j - Vi] + Ci)

    return dp[K]

# 테스트 케이스 입력 및 처리
T = int(input())  # 테스트 케이스 수 입력
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 물건의 개수와 가방의 최대 부피
    items = [tuple(map(int, input().split())) for _ in range(N)]  # 각 물건의 부피와 가치 입력

    # 최대 가치 계산
    result = knapsack(N, K, items)
    print(f"#{test_case} {result}")
