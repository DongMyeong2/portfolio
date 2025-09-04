S=int(input())
N=0
test = 0

while True:
  if S==test:
    break
  elif S<test:
    N=N-1
    break
  else:
    N+=1
    test = test + N
    
print(N)