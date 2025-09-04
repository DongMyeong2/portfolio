word = list(input())
while len(word) != 0:
  if len(word) < 10:
    print("".join(word))
    word=[]
  else:
    print("".join(word[0:10]))
    word=word[10::]