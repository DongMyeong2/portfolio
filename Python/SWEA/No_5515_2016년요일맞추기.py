
T = int(input())

for test_case in range(1, T + 1):
    m, n = map(int, input().split()) # m : 월, n : 일
    n += 3 # 1월 1일이 금요일이므로 2015년 12월 31일을 목요일로 시작 
    calendar = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    for i in range(1, m): # 입력 받은 달의 전달까지를 모두 일로 바꾸어 더함
        n+=calendar[i]
    print("#"+str(test_case), n%7) # 7로 나눴을 떄의 나머지가 구하는 값
