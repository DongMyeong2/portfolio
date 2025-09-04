
import math

def find_min_b(A):
    factors = {}
    num = A
    d = 2

    # 소인수 분해
    while d * d <= num:
        while (num % d) == 0:
            factors[d] = factors.get(d, 0) + 1
            num //= d
        d += 1
    if num > 1:
        factors[num] = factors.get(num, 0) + 1

    # 최소의 B 구하기
    B = 1
    for factor, count in factors.items():
        if count % 2 != 0:
            B *= factor
    return B

T = int(input())
results = []

for test_case in range(1, T + 1):
    A = int(input())
    B = find_min_b(A)
    results.append(f"#{test_case} {B}")

# 결과 한 번에 출력
print("\n".join(results))
