
T = int(input())
# n번 때렸을 떄, 다음 공격이 몬스터에게 입히는 데미지 : D(1+n*L* (1/100))
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split()) # D : 기본 데미지, L : 레벨당 추가 데미지, N : 공격 횟수
    damage = 0
    for i in range(N):
        damage += D * ( 1 + ( i * L * (1/100)))
    print("#"+str(test_case), int(damage))
