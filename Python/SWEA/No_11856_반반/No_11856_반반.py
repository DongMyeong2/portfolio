
# TIP : set을 이용하여 중복된 요소 없는 리스트 만들기

T = int(input())

for test_case in range(1, T + 1):
    word = list(set(input()))
    if len(word) == 2:
        print("#"+str(test_case), "Yes")
    else:
        print("#"+str(test_case), "No")
