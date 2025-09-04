
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    limit = 999
    check = [True] * (limit+1)
    check[0] = check[1] = False
    prime = []

    # 소수인 값만 True로
    for i in range(2, int(limit**0.5)+1):
        if check[i]:
            # i의 배수는 소수가 아니므로 False로 마킹
            for j in range(i * i, limit + 1, i):
                check[j] = False

    # True인 값의 인덱스가 소수
    for i in range(limit+1):
        if check[i]:
            prime.append(i)

    count = 0
    for F in range(len(prime)):
        for S in range(F, len(prime)):
            for D in range(S, len(prime)):
                if prime[F]+prime[S]+prime[D] == N:
                    count+=1
                    break                
    print("#"+str(test_case), count)
