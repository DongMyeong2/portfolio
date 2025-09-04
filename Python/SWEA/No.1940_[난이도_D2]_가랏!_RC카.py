T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    distance = 0
    current = 0 # 현재 속도
    for _ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 0:
            distance += current
        elif command[0] == 1:
            current+=command[1]
            distance +=current
        elif command[0] == 2:
            if current <= command[1]:
                current = 0
            else:
                current -= command[1]
                distance += current
    print(f"#{test_case} {distance}")