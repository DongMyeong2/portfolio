
T = int(input())

for test_case in range(1, T + 1):
    number = list(input())
    check = int("".join(number))
    number.sort()
    result = 2

    while True:
        number_mul = list(str(result * check))
        if len(number_mul) > len(number):
            print("#"+str(test_case), "impossible")
            break
        number_mul.sort()
        if number == number_mul:
            print("#"+str(test_case), "possible")
            break
        result +=1
