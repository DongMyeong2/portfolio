
T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    s1, s2 = input().split()  # 두 문자열 입력
    m, n = len(s1), len(s2)   # 각 문자열의 길이 계산

    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: # 같은 문자가 있으면 대각선에서 +1
                dp[i][j] = dp[i - 1][j - 1] + 1  
            else: # 아니면 위쪽 또는 왼쪽에서 큰 값 선택
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  

    # 최종 결과 출력
    print(f"#{tc} {dp[m][n]}")
