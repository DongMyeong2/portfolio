
# TIP : N의 제곱근까지만 반복하여 확인함으로서 실행 시간을 줄임
#       제곱근 구할 때 int(N**0.5) 사용해도 가능 

import math

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = N - 1
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            if (N // i) + i -1 < result:
                result = (N // i) + i -2
    print("#"+str(test_case), result)
