# TIP : 입력 받은 월을 전월까지의 마지막 날 합으로 할당
# EX : 3월을 입력 받으면 3을 1월의 마지막날 31과 2월의 마지막날 28의 합인 59로 바꾼다.
T = int(input())

for test_case in range(1, T + 1):
    Last_Day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Month_Day = list(map(int, input().split()))
    
    First_Month = sum(Last_Day[:Month_Day[0]-1])
    First_Day = Month_Day[1]
    
    Second_Month = sum(Last_Day[:Month_Day[2]-1])
    Second_Day = Month_Day[3]
    
    result = (Second_Month - First_Month) + (Second_Day - First_Day)
    
    print("#"+str(test_case), result+1)