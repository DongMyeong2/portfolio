T = int(input())
n = [int(input()) for _ in range(T)]
max_num = max(n)

is_prime = [True] * (max_num + 1)
is_prime[0] = is_prime[1] = False 

for i in range(2, int(max_num**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

# 소수를 set에 저장하여 빠르게 접근
primes = {i for i in range(2, max_num + 1) if is_prime[i]}

for i in n:
    ans = 0
    for j in range(2, i // 2 + 1):
        if j in primes and (i - j) in primes:
            ans += 1
    print(ans)