
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  
    numbers = []  # N개의 숫자를 저장할 리스트
    stop = False

    # N개의 정수를 입력받는 부분
    while len(numbers) < N:  # N개의 숫자를 입력받을 때까지 반복
        numbers.extend(input().split())

    # 0이 입력받은 리스트에 있는 경우 0보다 크고 리스트에 없는 값 중 가장 작은 값 찾기
    if '0' in numbers:
        # i는 자릿수를 나타낸다 -> i=1이면 만들 수 있는 한 자릿수
        for i in range(1, N+1):
            result = []
            for j in range(N-i+1):
                result.append(int("".join(numbers[j:j+i])))
            # i=1일 때 -> 1~9까지 검사, i=2일 때 -> 10~99까지 검사
            for k in range( 10**(i-1), 10**i):
                if k not in result:
                    Output = k
                    stop = True
                    break
            if stop:
                print("#"+str(test_case), Output)
                break
    else:
        print("#"+str(test_case), 0)
