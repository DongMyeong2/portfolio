INPUT = list(map(str, input().split("-")))
result = []

for i in range(len(INPUT)):
  NAME =list(INPUT[i])
  result.append(NAME[0])
  
print("".join(result))