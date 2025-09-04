from bisect import bisect_left, bisect_right

def count_occurrences(arr, x):
    left = bisect_left(arr, x)  # x의 첫 번째 위치
    right = bisect_right(arr, x)  # x의 마지막 위치 바로 뒤
    return right - left  # x의 개수 (등장하는 횟수)

N = int(input())
N_num = list(map(int, input().split()))
N_num.sort()  # 정렬

M = int(input())
M_num = list(map(int, input().split()))

result = [count_occurrences(N_num, num) for num in M_num]
print(" ".join(map(str, result)))