
T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 버스 노선의 수
    road = [] # 노선에 들어가는 정류장 번호를 담은 리스트
    result = [] # P_i 정류장을 지나는 노선의 수를 담은 리스트

    for _ in range(N):
        start, end = map(int, input().split())
        road.append([ x for x in range(start, end+1)])

    P = int(input())

    for _ in range(P):
        P = int(input())
        count = 0
        for road_list in road: # 해당 정류장이 노선에 포함되면 1 증가
            if P in road_list:
                count+=1
        result.append(count)

    print("#"+str(test_case), " ".join(map(str, result)))
