# TIP : max 함수를 사용하여 주위의 빌딩 중 가장 높은 빌딩만 고려하여
#       현재 빌딩과의 차를 통해서 원하는 바를 구하자.

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    Height = list(map(int, input().split()))
    result = 0
    
    for i in range(2, N-2):
        # 현재 빌딩의 양옆 두 칸과 비교하여 가장 작은 값을 구함
        max_neighbor_height = max(Height[i-2], Height[i-1], Height[i+1], Height[i+2])
        
        # 현재 빌딩이 이 값보다 클 경우 조망권이 확보된 부분을 계산
        if Height[i] > max_neighbor_height:
            result += Height[i] - max_neighbor_height

    print("#" + str(test_case), result)