
T = int(input())

for test_case in range(1, T + 1):
    Day = {'MON' : 1, 'TUE' : 2, 'WED' : 3, 'THU' : 4, 'FRI' : 5, 'SAT' : 6, 'SUN' : 0}
    Input_Day = input()
    print("#"+str(test_case), 7-Day[Input_Day])
