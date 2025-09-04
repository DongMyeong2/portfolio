import math

N = int(input())
count = 0

num=list(str(math.factorial(N)))
reverse_num=num[-1::-1]

for i in range(len(reverse_num)):
  if reverse_num[i] == "0":
    count+=1
  elif reverse_num[i] != "0":
    break
print(count)