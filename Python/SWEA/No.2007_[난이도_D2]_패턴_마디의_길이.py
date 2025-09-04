# TIP : 마디 하나씩 늘려가며 다음에 나오는 패턴이 동일하면 멈추고 마디 길이 출력

T = int(input())

for test_case in range(1, T + 1):
    Word = input()
    Word_list=list(Word)
    for i in range(1, 10): # 조건에서 최대 마디의 길이가 10이므로 최대 10번 반복
        if Word_list[:i] == Word_list[i:2*i] :
            print("#"+str(test_case), i)
            break