Word=list(input())

for i in range(len(Word)):
  if Word[i].isupper():
    Word[i]=Word[i].lower()
  elif Word[i].islower():
    Word[i]=Word[i].upper()
print("".join(Word))