# TIP : 맨뒤에서부터 탐색하며 최대 매매가로 얻을 수 있는 이윤 더해나가기

T = int(input())  # 테스트 케이스 수 입력

for test_case in range(1, T + 1):
    N = int(input())  # 날짜 수 입력
    prices = list(map(int, input().split()))  # 매매가 입력
    
    max_profit = 0
    max_price = 0
    
    # 매매가를 뒤에서부터 탐색
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            max_profit += max_price - prices[i]
    
    print(f"#{test_case} {max_profit}")
