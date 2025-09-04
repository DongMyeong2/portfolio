N = int(input())

lst = [i for i in range(1, N+1)]
now = 0
t = 1

while len(lst) > 1:
    t_3 = t ** 3 - 1
    now = (now + t_3 % len(lst)) % len(lst)
    lst.pop(now)
    t += 1
    
print(lst[0])