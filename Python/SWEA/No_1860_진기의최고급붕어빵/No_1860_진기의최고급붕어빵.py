
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N : 맛보는 사람 수
    # M초의 시간을 동안 K개의 붕어빵을 만듦
    people = list(map(int, input().split()))
    people.sort()
    result = {}
    possible = True

    # 도착한 시간에 만들어져 있을 붕어빵의 수
    for i in range(len(people)):
        result[i] = (people[i]//M)*K

    # 이미 먹고 간 사람들의 붕어빵을 뺀 현재 남아있는 붕어빵의 수
    for i in range(len(people)):
        result[i] -= i
        # 붕어빵이 없다면 Impossible
        if result[i] == 0:
            possible = False
            break

    if possible:
        print("#"+str(test_case), "Possible")
    else:
        print("#"+str(test_case), "Impossible")
