K = int(input())

for i in range(1,K+1):
  GAP = []
  INPUT = list(map(int, input().split()))
  score=INPUT[1::]
  score.sort()
  for j in range(1, len(score)):
    GAP.append(score[j]-score[j-1])
  print("Class", i)
  print("Max", str(max(score))+",", "Min", str(min(score))+",", "Largest gap", max(GAP))