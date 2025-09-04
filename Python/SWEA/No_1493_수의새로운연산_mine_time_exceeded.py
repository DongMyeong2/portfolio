
# 내 풀이 -> 계산마다 리스트를 생성해서 제한 시간 초과
def cal_1(p, q):
    matrix = []
    var = 1
    while len(matrix) < max(p,q):
        for i in range(var):
            matrix.append([i+1, var - i])
        var += 1
    return matrix

def cal_2(cal):
    matrix = []
    var = 1
    while cal not in matrix:
        for i in range(var):
            matrix.append([i+1, var - i])
        var += 1
    return matrix

T = int(input())

for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    cal = []

    for i in range(2):
        cal.append(cal_1(p, q)[p-1][i]+cal_1(p, q)[q-1][i])
    print("#"+str(test_case), cal_2(cal).index(cal)+1)
