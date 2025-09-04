
import math

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(input().split())
    M_list = list(input().split())
    Q = int(input())

    print("#"+str(test_case), end = " ")
    for _ in range(Q):
        year = int(input())
        print( N_list[(year%N) - 1]+M_list[(year%M) - 1], end = " ")
    print()
