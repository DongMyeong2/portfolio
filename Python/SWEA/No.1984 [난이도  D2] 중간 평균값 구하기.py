# case 1 : round 이용하여 반올림한 값 구하기
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    num.remove(max(num))
    num.remove(min(num))
    result = sum(num) / 8
    print("#" + str(test_case), int(round(result, 0)))

# case 2
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    num.remove(max(num))
    num.remove(min(num))
    result = sum(num) / 8
    if int(result) + 0.5 > result:
        print("#" + str(test_case), int(result))
    elif int(result) + 0.5 <= result:
        print("#" + str(test_case), int(result) + 1)