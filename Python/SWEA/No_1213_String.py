
for test_case in range(10):
    T = int(input())
    find = input()
    string = input()
    count = 0
    for i in range(len(string)-len(find)+1):
        if string[i:i+len(find)] == find:
            count+=1
    print("#"+str(T), count)
