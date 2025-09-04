
# TIP : 어떤 수의 배수는 소수가 아님
#       이를 구현하는 방법 숙지하기!

T = int(input())

for test_case in range(1, T + 1):
    D, A, B = map(int, input().split())
    prime = [True] * (B+1)
    prime[0] = prime[1] = False
    count = 0

    for i in range(2, int(B**0.5)+1):
        if prime[i]:
            # i의 배수는 소수가 아니므로 False로 마킹
            for j in range(i * i, B + 1, i):
                prime[j] = False

    for i in range(A, B+1):
        if prime[i] and str(D) in str(i):
            count+=1

    print("#"+str(test_case), count)
