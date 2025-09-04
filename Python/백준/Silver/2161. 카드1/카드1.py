N = int(input())

lst = [i for i in range(1, N+1)]
result = []

while len(lst) > 1:
    result.append(lst.pop(0))
    lst.append(lst.pop(0))
result.append(lst.pop(0))

print(" ".join(map(str, result)))