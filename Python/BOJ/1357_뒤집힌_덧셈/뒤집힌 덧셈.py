X, Y = map(str, input().split())

X_list = list(X)
Y_list = list(Y)

X_reverse = int("".join(X_list[-1::-1]))
Y_reverse = int("".join(Y_list[-1::-1]))

result = list(str(X_reverse+Y_reverse))

print(int("".join(result[-1::-1])))