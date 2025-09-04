
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = [1,2,3,4,5,6,7,8,9]
    quo = [] # 몫
    result = 0 # 1 이상 9 이하의 두 수의 곱으로 표현할 수 있는 경우의 수

    for i in range(1, 10):
        if n % i == 0:
            quo.append(n // i)

    for i in range(len(quo)):
        if quo[i] in nums:
            result +=1
    if result:
        print("#"+str(test_case), "Yes")
    else:
        print("#"+str(test_case), "No")
