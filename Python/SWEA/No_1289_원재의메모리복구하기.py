
T = int(input())

for test_case in range(1, T + 1):
    mem = list(input())
    count = 0
    for i in range(len(mem)):
        if mem[i] == '1':
            count+=1
            for j in range(i, len(mem)):
                if mem[j] == '1':
                    mem[j] = '0'
                elif mem[j] == '0':
                    mem[j] = '1'
    print("#"+str(test_case), count)
