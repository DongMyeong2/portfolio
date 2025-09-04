from copy import deepcopy

N = int(input())
dp = [1]*10
dp[0] = 0

for _ in range(N-1):
    copy = deepcopy(dp)
    for i in range(10):
        if i == 0:
            dp[0] = copy[1]
        elif i == 9:
            dp[9] = copy[8]
        else:
            dp[i] = copy[i-1] + copy[i+1]

print(sum(dp)%1000000000)