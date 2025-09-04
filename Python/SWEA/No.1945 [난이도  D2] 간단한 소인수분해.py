# TIP : while문을 사용하여 나누어 떨어지지 않을때까지 반복해서 나누고 나눈 수는
#       다른 리스트로 추가

T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    num = [2, 3, 5, 7, 11]
    num_total = []
    result = []
    for i in num:
        while (N%i) == 0:
            num_total.append(i)
            N//=i
    for j in num:
        result.append(str(num_total.count(j)))
    print("#"+str(test_case), " ".join(result))