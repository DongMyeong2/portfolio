
# case 2 : math 패키지 사용하지 않았을 때

# 두 문자열 길이의 최소 공배수를 먼저 구하자

T = int(input())

for test_case in range(1, T + 1):
    S, T = input().split()

    # 문자열 길이 구하기
    S_len = len(S)
    T_len = len(T)

    # 최대 공약수와 최소 공배수 구하기
    for num in range(min(S_len, T_len), 0, -1):
        if (S_len % num == 0) and (T_len % num == 0):
            gcd = num
            break
    lcm = gcd * (S_len//gcd) * (T_len//gcd)

    # 최소 공배수 길이에 맞게 문자열 조정
    S, T = S * (lcm//S_len), T * (lcm//T_len)

    if S == T:
        print("#"+str(test_case), "yes")
    else:
        print("#"+str(test_case), "no")
