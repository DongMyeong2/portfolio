
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    word = [ input() for _ in range(N) ]
    half_pal = 0 # 다른 문자열과 만났을 때 팰린드롬이 되는 문자열 (2개씩 세트)
    pal = 0 # 스스로 팰린드롬인 문자열
    nothing = 0 # 팰린드롬이 되지 않는 문자열

    while half_pal + pal + nothing != N:
        # pal 갯수 세아리기
        if word[0] == word[0][-1::-1]:
            pal += 1
            word.pop(0)
        # half_pal 갯수 세아리기
        elif word[0][-1::-1] in word[1:]:
            index = word[1:].index(word[0][-1::-1])
            half_pal += 2
            word.pop(0)
            word.pop(index)
        # nothing 갯수 세아리기
        else:
            nothing += 1
            word.pop(0)

    # 다른 문자열과 만나서 팰린드롬이 되는 문자열은 대칭을 이룸
    result = half_pal * M

    # 자기 스스로 팰린드롬인 문자열은 가운데 하나만 들어갈 수 있어서
    # 1개 이상이면 pal 값이 어떻든 문자열 길이만큼만 더함
    if pal > 0:
        result += M

    print("#"+str(test_case), result)
