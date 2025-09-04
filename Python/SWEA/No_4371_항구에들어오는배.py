
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    first_day = int(input())
    happy_day = []
    cycle = []

    for _ in range(N-1):
        happy_day.append(int(input()))

    for day in happy_day:
        plus = True
        if day - first_day not in cycle: # 배가 들어온 날이 주기에 안들어가 있을 때
            for cyl in cycle:
                if (day - first_day)%cyl == 0: # 주기에 안들어가 있으나 주기인 수의 배수일 때
                    plus = False
                    break
            if plus:
                cycle.append(day-first_day)

    print("#"+str(test_case), len(cycle))
