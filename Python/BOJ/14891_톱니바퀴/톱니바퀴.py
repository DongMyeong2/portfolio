matrix = []
for _ in range(4):
    matrix.append(list(input()))

dp = [[0] * 8] * 4

K = int(input())

for num in range(K):
    N, spin = map(int, input().split())
    if spin == 1:
        dp[N - 1] = [matrix[N - 1][-1]] + matrix[N-1][:-1]
    else:
        dp[N - 1] = matrix[N - 1][1:] + [matrix[N - 1][0]]

    spin_i = spin
    for i in range(N - 1, 0, -1):
        if matrix[i][-2] != matrix[i - 1][2]:
            if spin_i == 1:
                dp[i - 1] = matrix[i - 1][1:] + [matrix[i - 1][0]]
                spin_i = -1
            else:
                dp[i - 1] = [matrix[i - 1][-1]] + matrix[i - 1][:-1]
                spin_i = 1
        else:
            for k in range(i, 0, -1):
                dp[k - 1] = matrix[k - 1]
            break

    spin_j = spin
    for j in range(N - 1, 3):
        if matrix[j][2] != matrix[j + 1][-2]:
            if spin_j == 1:
                dp[j + 1] = matrix[j + 1][1:] + [matrix[j + 1][0]]
                spin_j = -1
            else:
                dp[j + 1] = [matrix[j + 1][-1]] + matrix[j + 1][:-1]
                spin_j = 1
        else:
            for l in range(j, 3):
                dp[l + 1] = matrix[l + 1]
            break
    matrix = dp.copy()

result = 0

for i in range(4):
    if matrix[i][0] == '1':
        result += 2**i
print(result)
