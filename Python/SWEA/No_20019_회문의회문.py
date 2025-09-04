
def pal(palindrome):
    if palindrome == palindrome[-1::-1]:
        return True
    else:
        return False

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    word_test = (len(word)-1)//2
    if pal(word) and pal(word[:word_test]) and pal(word[-1:len(word)-word_test-1:-1]):
        print("#"+str(test_case), "YES")
    else:
        print("#"+str(test_case), "NO")
