Alpha=list("abcdefghijklmnopqrstuvwxyz")
word=list(input())
for i in range(len(Alpha)):
  count=0
  for j in range(len(word)):
    if Alpha[i] == word[j]:
      count+=1
  Alpha[i]=str(count)
print(" ".join(Alpha))