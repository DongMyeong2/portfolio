Alpha=list("abcdefghijklmnopqrstuvwxyz")
Alpha_count=list("abcdefghijklmnopqrstuvwxyz")

word = input()
word = word.lower()

for i in range(len(Alpha)):
  Alpha_count[i]=word.count(Alpha_count[i])

if Alpha_count.count(max(Alpha_count)) == 1:
  print(Alpha[Alpha_count.index(max(Alpha_count))].upper())
else:
  print("?")