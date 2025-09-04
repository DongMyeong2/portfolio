
# GPT 풀이
def get_coordinates(n):
    #주어진 n에 대해 (x, y) 좌표를 계산하는 함수
    diagonal = 1
    while n > diagonal * (diagonal + 1) // 2:
        diagonal += 1
    offset = n - diagonal * (diagonal - 1) // 2
    x = offset
    y = diagonal - offset + 1
    return x, y

def get_number(x, y):
    #주어진 (x, y) 좌표에 대해 숫자를 계산하는 함수
    diagonal = x + y - 1
    return diagonal * (diagonal - 1) // 2 + x

def cal_star(p, q):
    x1, y1 = get_coordinates(p)
    x2, y2 = get_coordinates(q)
    new_x = x1 + x2
    new_y = y1 + y2
    return get_number(new_x, new_y)

# 입력 처리 및 출력
T = int(input())

for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    result = cal_star(p, q)
    print(f"#{test_case} {result}")
