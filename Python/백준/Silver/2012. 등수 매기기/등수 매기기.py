import sys

input = sys.stdin.read

# 입력 처리
data = input().split()
T = int(data[0])  # 첫 번째 값은 T
predict = list(map(int, data[1:]))  # 나머지 값은 예상 등수 리스트

# 예상 등수 정렬
predict.sort()

# 불만도의 합 계산
ans = 0
for i in range(1, T + 1):
    ans += abs(predict[i - 1] - i)

# 결과 출력
print(ans)