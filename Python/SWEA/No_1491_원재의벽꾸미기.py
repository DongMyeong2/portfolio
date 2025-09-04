
# TIP : N개 이하의 타일로 R * C 크기의 타일을 만들어야 하므로,
#       R * C <= N가 성립해야함

T = int(input())

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    result = []
    for r in range(1, N):
        for c in range(1, N):
            if r*c > N:
                break
            cal = A*abs(r-c)+B*(N-r*c)
            result.append(cal)
    print("#"+str(test_case), min(result))
