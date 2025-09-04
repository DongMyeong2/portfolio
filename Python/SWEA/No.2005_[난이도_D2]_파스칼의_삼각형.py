# TIP : 리스트의 처음과 끝은 1로 고정하고 중간 부분만 계산

T = int(input())

for test_case in range(1, T + 1):
    N =int(input())
    sol = [1]
    print("#"+str(test_case))
    for i in range(N):
        print(" ".join(map(str, sol))) # 정수로 된 리스트 문자열로 변환해서 join
        
        result = [1]
        for j in range(1, len(sol)):
            result.append(sol[j - 1] + sol[j])
        result.append(1)
        
        sol = result