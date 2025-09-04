def dfs(n, rabit, cat):
    global ans
    if n == N:
        # 두 리스트의 길이가 N이 되는지 확인하고 중복 방지를 위해 set에 추가
        if len(rabit) + len(cat) == N:
            state = (tuple(rabit), tuple(cat))
            if state not in ok:
                ok.add(state)
                ans += 1
        return
    
    # 조건에 맞는 분기
    if check[n] == len(rabit):
        dfs(n + 1, rabit + [n], cat)
    if check[n] == len(cat):
        dfs(n + 1, rabit, cat + [n])

# 입력 처리
N = int(input())
height = list(map(int, input().split()))
height.sort()

check = height  # check 리스트로 높이를 정리

ans = 0
ok = set()  # 중복 방지용 set

# DFS 호출
dfs(0, [], [])
print(ans)
