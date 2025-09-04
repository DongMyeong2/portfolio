while True:
  Triangle = list(map(int, input().split()))
  if Triangle[0] == Triangle[1] == Triangle[2] == 0:
    break
  
  Triangle.sort()

  if Triangle[2] >= Triangle[0]+Triangle[1]:
    print("Invalid")
  elif Triangle[0] == Triangle[1] == Triangle[2]:
    print("Equilateral")
  elif (Triangle[0] == Triangle[1]) or (Triangle[0] == Triangle[2]) or (Triangle[1] == Triangle[2]):
    print("Isosceles")
  else:
    print("Scalene")