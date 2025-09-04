while True:
  word=input()
  if word == "END":
    break
  else:
    result=list(word)
    print("".join(result[-1::-1]))