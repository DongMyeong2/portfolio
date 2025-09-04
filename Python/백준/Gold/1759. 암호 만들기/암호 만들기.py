def dfs(n, check):
    if len(check) == L:
        check.sort()
        count = 0
        for vowel in vowels:
            count += check.count(vowel)
        if count >= 1 and L - count >= 2:
            result.add("".join(check))
    if n == C:
        return
    dfs(n+1, check+[word[n]])
    dfs(n+1, check)

L, C = map(int, input().split())
word = list(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

result = set()
dfs(0, [])
result = list(result)
result.sort()

for out in result:
    print(out)