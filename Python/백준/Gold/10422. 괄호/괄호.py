MOD = 1000000007

def mod_inverse(x, mod):
    # 페르마의 소정리를 사용하여 x의 모듈러 역수 계산
    return pow(x, mod - 2, mod)

def check(N):
    if N % 2 != 0:
        return 0

    half_n = N // 2
    catalan = 1  # C_0 = 1

    for n in range(1, half_n + 1):
        # 점화식 적용: C_{n+1} = C_n * (2 * (2 * n - 1) / (n + 1))
        catalan = catalan * (2 * (2 * n - 1)) % MOD
        catalan = catalan * mod_inverse(n + 1, MOD) % MOD

    return catalan

# 입력 처리 및 결과 출력
T = int(input())
for _ in range(T):
    N = int(input())
    print(check(N))
