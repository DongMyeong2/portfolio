
T = int(input())

for test_case in range(1, T + 1):
    # n : 주차 공간의 수, m : 주차장을 이용할 차량의 수
    n, m = map(int, input().split())

    # R : i번째 주차공간의 무게당 요금
    R = [int(input()) for _ in range(n)] 

    # W : i번째 차량 무게
    W = {}
    for i in range(1, m+1):
        W[i]= int(input()) 

    wait = [] # 주차 공간이 없을 때 대기하는 i번째 차량들을 저장하는 리스트
    now = [0] * n # 주차 공간이 있으면 0 으로 표시
    result = 0 # 이익

    for i in range(2*m):
        x=int(input())
        if x > 0:
            if 0 in now: # 주차 공간이 있는 경우
                for i in range(n):
                    if now[i] == 0:
                        result += R[i] * W[x]
                        now[i]  = x
                        break
            else: # 주차 공간이 없는 경우
                wait.append(x)
        elif x < 0:
            now[now.index(abs(x))] = 0
            if wait: # 차량 한대가 빠져 나가 대기 차량이 있으면 주차시킨다 
                for i in range(n):
                    if now[i] == 0:
                        result += R[i] * W[wait[0]]
                        now[i]  = wait.pop(0)
                        break
    print("#"+str(test_case), result)
