
# TIP : A를 B로 나눈 몫을 한 변으로 하는 작은 삼각형이 큰 삼각형의 아래에 깔리고,
#       나머지 부분은 1부터 (A//B)-1까지 수를 2배 한 값들의 합만큼 채워짐 

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    result = A // B
    for i in range(1, result):
        result += i*2
    print("#"+str(test_case), result)
