T = int(input())

score = {"A":1, "B":2, "C":3, "D":4, "E":5,
         "F":6, "G":7, "H":8, "I":9, "J":10,
         "K":11, "L":12, "M":13, "N":14, "O":15,
         "P":16, "Q":17, "R":18, "S":19, "T":20,
         "U":21, "V":22, "W":23, "X":24, "Y":25,
         "Z":26}

for _ in range(T):
  X, Y = map(str, input().split())

  X_list = list(X)
  Y_list = list(Y)
  
  result=[]

  for i in range(len(X_list)):
    if X_list[i] <= Y_list[i]:
      result.append(str(score[Y_list[i]]-score[X_list[i]]))
    elif X_list[i] > Y_list[i]:
      result.append(str(score[Y_list[i]]+26-score[X_list[i]]))
  print("Distances:", " ".join(result))