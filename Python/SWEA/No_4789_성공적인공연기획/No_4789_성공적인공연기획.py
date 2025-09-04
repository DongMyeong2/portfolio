
T = int(input())

for test_case in range(1, T + 1):
    known = [ int(x) for x in input()]
    clap = 0 # 현재까지 박수친 인원
    need = 0 # 현재 필요한 직원 수
    result = 0 # 총 필요한 직원 수

    for i in range(len(known)):
        if i <= clap:
            clap += known[i]
        else:
            need = i - clap
            result += i - clap
            clap += known[i] + need

    print("#"+str(test_case), result)
