import math

s = input()
t = input()

lcm = math.lcm(len(s), len(t))

s, t = s*(lcm//len(s)), t*(lcm//len(t))

if s == t:
    print(1)
else:
    print(0)