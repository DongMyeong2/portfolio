def result(Time, Clock, Second):
    if Second >= 60:
        Second -= 60
        Clock += 1
    if Clock > 12:
        Clock -= 12
    result = [Clock, Second]
    return result

T = int(input())

for test_case in range(1, T + 1):
    Time = list(map(int, input().split()))
    Output = result(Time, Time[0]+Time[2], Time[1]+Time[3])
    print("#"+str(test_case), " ".join(map(str, Output)))