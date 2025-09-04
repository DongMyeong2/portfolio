
# TIP : max는 빈 리스트에 대해 사용할 때, 에러가 나옴

T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # N: 재료의 개수, L: 최대 칼로리
    ingredients = []  # 각 재료의 (점수, 칼로리)을 저장할 리스트

    for _ in range(N):
        score, cal = map(int, input().split())  # 재료의 점수와 칼로리 입력
        ingredients.append((score, cal))  # 튜플로 저장

    max_score = 0  # 가능한 최대 점수

    # 모든 부분집합을 순회하면서 계산
    for i in range(1 << N):  # 2^N개의 부분집합
        total_score = 0
        total_calories = 0

        for j in range(N):
            if i & (1 << j):  # i번째 부분집합에 j번째 재료가 포함되는 경우
                total_score += ingredients[j][0]  # 점수를 더함
                total_calories += ingredients[j][1]  # 칼로리를 더함

        # 칼로리가 L 이하인 경우만 최대 점수를 갱신
        if total_calories <= L:
            max_score = max(max_score, total_score)

    print(f"#{test_case} {max_score}")
