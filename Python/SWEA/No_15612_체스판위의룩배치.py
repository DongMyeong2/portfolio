
T = int(input())

for test_case in range(1, T + 1):
    board = [ list(input()) for _ in range(8) ]
    check = []
    count = 0
    result = True
    for row in range(8):
        count += board[row].count('O')
        if board[row].count('O') > 1:
            result = False
        for col in range(8):
            if board[row][col] == 'O':
                if col in check:
                    result = False
                    break
                check.append(col)
    if count != 8:
        result = False

    if result:
        print("#"+str(test_case), "yes")
    else:
        print("#"+str(test_case), "no")
