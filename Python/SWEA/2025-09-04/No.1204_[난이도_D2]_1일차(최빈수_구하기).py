# TIP : 딕셔너리의 value를 리스트 안에 있는 점수로 하고 해당 점수의 수를 세아려
#       그 수를 key값으로 한다. for문이 돌아가며 최빈값의 value는 알아서 큰 값으로 변경

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    score_count = {}
    for i in range(min(score), max(score)+1):
        score_count[score.count(i)]=i
    result = score_count[max(score_count)]
    print("#"+str(test_case), result)