N = int(input())
word = input()

# dp 배열 초기화
dp = [N*N] * N
dp[0] = 0  # 시작점 초기화

# BOJ 패턴 설정
BOJ = 'BOJ'

for i in range(N):
    # 현재 위치의 글자가 BOJ 패턴 중 어디에 해당하는지 찾기
    current_index = BOJ.index(word[i])
    next_char = BOJ[(current_index + 1) % 3]

    # 현재 위치에서 오른쪽으로 점프
    for j in range(i + 1, N):
        if word[j] == next_char:
            jump_cost = (j - i) ** 2
            dp[j] = min(dp[j], dp[i] + jump_cost)

print(dp[N - 1] if dp[N - 1] != N*N else -1)