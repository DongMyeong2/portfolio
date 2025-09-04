
# TIP : A와 B 중 작은 값으로 C를 나눈 몫이 구하려는 값과 같음

T = int(input())

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    if A <= B:
        result = C//A
    elif A > B:
        result = C//B
    print("#"+str(test_case), result)
