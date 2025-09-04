
# TIP : 끝에서부터 확인

T = int(input())

for test_case in range(1, T + 1):
    box = list(map(int, input().split()))
    result = 0
    for i in range(2, 0, -1):
        if box[i] == 1:
            result = -1
            break
        else:
            if box[i] <= box[i-1]:
                result += (box[i-1] - box[i]) + 1
                box[i-1] = box[i]-1
    print("#"+str(test_case), result)
