n = int(input())
Info_result = []
for _ in range(n):
    name, month, day, year = map(str, input().split())
    Info_ex = [name, int(month), int(day), int(year)]
    Info_result.append(Info_ex) # 리스트 안에 리스트 담기

Info_result.sort(key = lambda x:(x[3], x[2], x[1]))

print(Info_result[-1][0], Info_result[0][0], sep = "\n")