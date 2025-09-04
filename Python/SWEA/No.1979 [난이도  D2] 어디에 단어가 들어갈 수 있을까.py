# TIP : 전치행렬 이용

# case 1 : 내 풀이
def ROW(BOX, pattern, N, M):
    count = 0
    for i in range(N):
        for j in range(N-M+1):
            if j == 0:
                if BOX[i][j:j+M] == pattern:
                    if BOX[i][j+M] ==0:
                        count+=1
            elif j == N-M:
                if BOX[i][j:j+M] == pattern:
                    if BOX[i][j-1] == 0:
                        count += 1
            else:
                if BOX[i][j:j+M] == pattern:
                    if (BOX[i][j-1] == 0) and (BOX[i][j+M] ==0):
                        count +=1
    return count

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    BOX = []
    BOX_reverse = []
    pattern = []
    
    for _ in range(M):
        pattern.append(1)
        
    for _ in range(N):
        BOX.append(list(map(int, input().split())))
        
    BOX_reverse = [list(row) for row in zip(*BOX)] # 전치행렬 구하기
    # BOX_reverse = list(zip(*BOX))
    
    print("#"+str(test_case), ROW(BOX, pattern, N, M)+ROW(BOX_reverse, pattern, N, M))
    
    
# case 2 : 다른 풀이 -> 1이 나오면 계속 진행하고 정확히 M의 갯수만큼 1이 연속될 때 count
def count(arr):
    ret = 0  # K길이의 단어가 들어갈 수 있는 자리 개수
    for lst in arr:
        cnt = 0  # 연속된 1의 개수를 세기 위한 변수
        for j in range(len(lst)):
            if lst[j]:  # lst[j]가 1이면 (흰색 칸이면)
                cnt += 1  # 연속된 1의 개수를 증가
            else:  # lst[j]가 0이면 (검은색 칸이면)
                if cnt == K:  # 연속된 1의 개수가 K이면
                    ret += 1  # 단어가 들어갈 수 있는 자리로 카운트
                cnt = 0  # 연속이 끊기므로 cnt 초기화
        # lst 끝까지 확인했을 때 연속된 1의 개수가 K인 경우 추가
        if cnt == K:
            ret += 1
    return ret  # 가능한 자리를 반환

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 퍼즐 크기 N, 단어 길이 K 입력
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
    
    # arr: 퍼즐 배열, 각 행의 끝에 0을 추가하여 경계 처리를 쉽게 함
    # 마지막에 한 줄 더 추가하여 열 방향에서도 경계 처리가 가능하게 함

    arr_t = list(zip(*arr))  # 행렬을 전치하여 세로 방향을 가로처럼 처리하기 쉽게 변환
    
    ans = count(arr) + count(arr_t)  # 가로와 세로 방향의 가능한 자리를 더함

    print(f'#{test_case} {ans}')  # 결과 출력