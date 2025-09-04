
T = int(input())

for test_case in range(1, T + 1):
    case, total = input().split()
    GNS = {0: 'ZRO', 1: "ONE", 2:  "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
    num = list(input().split())
    result = []
    # 입력받은 문자열과 GNS의 value가 일치하면 key값을 result 리스트에 추가하고 정렬
    for i in range(int(total)):
        for j in range(10):
            if num[i] == GNS[j]:
                result.append(j)
    result.sort()
    print("#"+str(test_case))
    for i in range(int(total)):
        print(GNS[result[i]], end = " ")
    print()
