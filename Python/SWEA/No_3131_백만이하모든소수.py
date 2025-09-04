
# TIP : 현재 값의 배수는 소수가 아닌 것으로 처리하여 계산 속도를 줄임

limit = 1000000
check = [True] * limit # True면 소수이고, False이면 소수가 아니다.
check[0] = False # 1은 소수가 아니다

for index in range(2, limit+1):
    num = 2
    # 현재 값의 배수들은 소수가 아니다.
    while index * num <= limit:
        if check[index * num-1]:
            check[index * num-1] = False
        num+=1
result = [ x+1 for x in range(limit) if check[x]]
print(" ".join(map(str, result)))
