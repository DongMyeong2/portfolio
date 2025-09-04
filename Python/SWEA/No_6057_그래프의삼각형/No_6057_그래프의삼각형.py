
# 삼각형의 개수를 세는 함수
def count_triangles(N, edges):
    # 인접 행렬 생성 (N+1 크기로, 1-based index를 위해 0번째는 사용 안함)
    adj = [[0] * (N + 1) for _ in range(N + 1)]

    # 간선 정보 입력 (양방향 그래프)
    for x, y in edges:
        adj[x][y] = 1
        adj[y][x] = 1

    triangle_count = 0

    # 모든 i < j < k 조합에 대해 삼각형 여부 확인
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            if adj[i][j]:  # i와 j가 연결되어 있는 경우
                for k in range(j + 1, N + 1):
                    if adj[i][k] and adj[j][k]:  # i와 k, j와 k가 모두 연결되어 있으면 삼각형
                        triangle_count += 1

    return triangle_count

# 테스트 케이스 입력 처리
T = int(input())  # 테스트 케이스 수 입력
for test_case in range(1, T + 1):
    # N: 정점의 수, M: 간선의 수
    N, M = map(int, input().split())

    # 간선 정보 입력
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # 삼각형 개수 계산
    result = count_triangles(N, edges)

    # 결과 출력
    print(f"#{test_case} {result}")
