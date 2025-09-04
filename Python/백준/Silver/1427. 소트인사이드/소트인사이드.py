num=list(input())
result=[]
for i in range(len(num)):
  result.append(int(num[i]))

result.sort(reverse=True)

for i in range(len(num)):
  num[i]=str(result[i])

print("".join(num))