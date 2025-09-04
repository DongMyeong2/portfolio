N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 이진 탐색의 시작점과 끝점 설정
left, right = 0, max(lst)
result = 0

while left <= right:
    mid = (left + right) // 2  # 중간값을 톱의 높이로 설정
    check = sum((tree - mid) for tree in lst if tree > mid)  # 톱 높이로 자른 나무 길이의 합

    if check >= M:  # 원하는 길이 이상을 얻은 경우
        result = mid  # 현재 높이를 저장하고, 더 높은 높이에서 탐색
        left = mid + 1
    else:  # 원하는 길이보다 적은 경우
        right = mid - 1

print(result)
