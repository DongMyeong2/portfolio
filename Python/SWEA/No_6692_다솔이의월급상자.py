
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ave = []
    for _ in range(N):
        p, x = map(float, input().split()) 
        ave.append(p * x)
    print("#"+str(test_case), sum(ave))
