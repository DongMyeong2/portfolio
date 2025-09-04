
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    pi = list(map(int, input().split()))
    count = 0
    # index가 i일 때 바로 양옆과 비교
    for i in range(1, len(pi)-1):
        if pi[i] < max(pi[i-1], pi[i+1]) and pi[i] > min(pi[i-1], pi[i+1]):
            count+=1
    print("#"+str(test_case), count)
