
# 메모이제이션을 이용하여 교환했던 경우는 스킵 -> 시간 복잡도를 줄인다.

def dfs(count):
    global ans

    current_value = int("".join(dp))

    # 이미 이 상태에서 count 횟수를 남기고 나온 결과가 있다면 종료
    if (current_value, count) in visited:
        return
    visited.add((current_value, count))

    # 만약 교환을 다 했다면 최대값 갱신
    if count == 0:
        ans = max(ans, current_value)
        return

    # 모든 자리 쌍을 교환
    for i in range(len(dp)):
        for j in range(i + 1, len(dp)):
            dp[i], dp[j] = dp[j], dp[i]
            dfs(count - 1)
            dp[i], dp[j] = dp[j], dp[i]

T = int(input()) 

for test_case in range(1, T + 1):
    number, swap_count = input().split()
    dp = list(number)  
    swap_count = int(swap_count)

    visited = set()  # 중복 상태를 저장하는 집합
    ans = 0  # 가능한 최대값을 저장할 변수

    dfs(swap_count)

    print(f"#{test_case} {ans}")
