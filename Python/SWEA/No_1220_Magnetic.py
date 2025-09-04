
# TIP : 처음 주어졌을 때 1이 행렬의 아래쪽 끝이고, 2가 위쪽 끝이면 빼줘야하는데
#       전치행렬을 취하면 1은 오른쪽 끝으로, 2는 왼쪽 끝으로 빼주면 된다.

#       두 리스트를 join으로 합치면서 split(0)으로 하여 문자열로 반환한 후
#       check = 12로 해서 문자열로 비교해도 무방
T = 10

for test_case in range(1, T+1):
    size = int(input())
    count = 0
    check = [1, 2]
    matrix = []
    for _ in range(size):
        matrix.append(list(map(int, input().split())))
    # 전치행렬
    matrix_reverse = [list(row) for row in zip(*matrix)]

    # 움직이면 결국 빈공간 없이 맞닿게 되므로 빈공간 삭제
    for i in range(size): 
        while 0 in matrix_reverse[i]:
            matrix_reverse[i].remove(0)


    for i in range(size):
        # 왼쪽 끝에는 N극(1)이 있어야하므로 S극(2)이 있으면 삭제
        while matrix_reverse[i][0] == 2:
            matrix_reverse[i].pop(0)

        # 오른쪽 끝에는 S극(2)이 있어야하므로 N극(1)이 있으면 삭제
        while matrix_reverse[i][-1] == 1:
            matrix_reverse[i].pop(len(matrix_reverse[i])-1)

        # 위 과정에서 자성체가 더 이상 움직이지 경우 완성
        # check = [1, 2]의 수는 교착 상태의 수와 같음
        for j in range(len(matrix_reverse[i])-1):
            if  matrix_reverse[i][j:j+2] == check:
                count+=1

    print("#"+str(test_case), count)
