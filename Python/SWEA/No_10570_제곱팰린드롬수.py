
# TIP : 입력 받는 수 중 큰 수인 B보다 작은 제곱수만 골라내서 문제 해결에 사용

import math

# B보다 작은 제곱수로만 이루어진 리스트를 반환하는 함수
def num(A, B): 
    num = []
    i =1
    while i**2 <= B:
        if i ** 2 >= A:
            num.append(i**2)
        i+=1
    return num

# num 함수에서 반환된 리스트의 각 원소의 제곱근으로 이루어진 리스트를 반환하는 함수
def num_sqrt(num): 
    num_sqrt = []
    for i in range(len(num)):
        num_sqrt.append(int(math.sqrt(num[i])))
    return num_sqrt

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    count = 0

    for i in range(len(num(A,B))):
        result = list(str(num(A,B)[i]))
        result_sqrt = list(str(num_sqrt(num(A,B))[i]))
        # num 함수가 반환한 리스트가 회문인 경우
        if result == result[-1::-1]: 
            # num_sqrt 함수가 반환한 리스트가 회문인 경우
            if result_sqrt == result_sqrt[-1::-1]: 
                count+=1
    print("#"+str(test_case), count)
