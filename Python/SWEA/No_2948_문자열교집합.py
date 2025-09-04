
# set 자료형에서 '&'를 이용하여 교집합 구하기

T = int(input())

# 각 테스트 케이스 처리
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    set1 = set(input().split())
    set2 = set(input().split())

    # 두 집합의 교집합을 구하고 그 크기를 저장
    result = len(set1 & set2)

    print(f"#{test_case} {result}")
