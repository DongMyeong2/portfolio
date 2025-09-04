score = []
SUM=[]
INDEX=[]

for _ in range(8):
  N=int(input())
  score.append(N)

for _ in range(5):
  INDEX.append(str(score.index(max(score))+1))
  SUM.append(max(score))
  score[score.index(max(score))]= 0

INDEX.sort()

print(sum(SUM))
print(" ".join(INDEX))