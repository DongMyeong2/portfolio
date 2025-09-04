def cal(operator):
    result = A[0]
    for i in range(N-1):
        if operator[i] == '+':
            result += A[i+1]
        elif operator[i] == '-':
            result -= A[i+1]
        elif operator[i] == '*':
            result *= A[i+1]
        elif operator[i] == '/':
            if result <0:
                result = -(abs(result) // A[i+1])
            else:
                result //= A[i+1]
    return result
    
def dfs(n, operator):
    global ans
    if n == N-1:
        if operator.count("+") == count[0] and operator.count("-") == count[1] and operator.count("*") == count[2] and operator.count("/") == count[3]:
            ans[0] = max(ans[0], cal(operator))
            ans[1] = min(ans[1], cal(operator))
        return
    dfs(n+1, operator+['+'])
    dfs(n+1, operator+['-'])
    dfs(n+1, operator+['*'])
    dfs(n+1, operator+['/'])

N = int(input())
A = list(map(int, input().split()))
count = list(map(int, input().split()))

ans = [-1000000000, 1000000000]

dfs(0, [])

print(ans[0])
print(ans[1])