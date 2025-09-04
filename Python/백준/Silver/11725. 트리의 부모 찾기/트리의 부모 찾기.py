import sys
input = sys.stdin.readline

def iterative_dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in lst[node]:
            if result[neighbor] == 0:  # 아직 부모가 설정되지 않은 경우
                result[neighbor] = node  # 부모를 현재 노드로 설정
                stack.append(neighbor)

# 입력 처리
N = int(input())
lst = [[] for _ in range(N + 1)]
result = [0] * (N + 1)  # 각 노드의 부모를 저장할 배열

# 트리 구성
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# DFS 호출
result[1] = 1  # 루트 노드 1의 부모는 자기 자신으로 설정
iterative_dfs(1)

# 결과 출력 (2번 노드부터 N번 노드까지의 부모 출력)
for num in range(2, N + 1):
    print(result[num])