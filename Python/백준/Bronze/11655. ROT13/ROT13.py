ROT13 = list(input())

Alpha_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Alpha_lower = list("abcdefghijklmnopqrstuvwxyz")

for i in range(len(ROT13)):
  if ROT13[i] in Alpha_upper:
    if Alpha_upper.index(ROT13[i])+13 > 25:
      ROT13[i]=Alpha_upper[Alpha_upper.index(ROT13[i])-13]
    else:
      ROT13[i]=Alpha_upper[Alpha_upper.index(ROT13[i])+13]
  elif ROT13[i] in Alpha_lower:
    if Alpha_lower.index(ROT13[i])+13 > 25:
      ROT13[i]=Alpha_lower[Alpha_lower.index(ROT13[i])-13]
    else:
      ROT13[i]=Alpha_lower[Alpha_lower.index(ROT13[i])+13]
print("".join(ROT13))