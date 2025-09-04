
# TIP : 자른 통나무의 둘 중 큰 값이 2가 되도록 하는 사람이 이긴다.
#       둘이서 자르는데 N이 짝수이면 Alice가 2를 만들어 이기고, 홀수이면 Bob이 이긴다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    if N % 2 ==0:
        print("#"+str(test_case), "Alice")
    else:
        print("#"+str(test_case), "Bob")
