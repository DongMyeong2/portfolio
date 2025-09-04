
T = int(input())

for test_case in range(1, T + 1):
    check = ['(|', '|)', '()']
    field = input()
    count = 0
    for i in range(len(field) -1):
        for j in range(len(check)):
            if check[j] == field[i:i+2]:
                count +=1
    print("#"+str(test_case), count)
