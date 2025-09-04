T = int(input())

game = ['3', '6', '9']
result = []

for test_case in range(1, T + 1):
    num = []
    count = 0
    num = list(str(test_case))
    for i in range(len(num)):
        if num[i] in game:
            count +=1
    if count == 0:
        result.append(str(test_case))
    elif count > 0:
        result.append("-"*count)
print(" ".join(result))