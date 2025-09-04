def student_score(score):  # N/10 명의 학생들에게 동일한 학점을 부여하기 위한 함수
    result = []
    for i in range(10):
        for _ in range(N // 10):
            result.append(score[i])
    return result


T = int(input())

for test_case in range(1, T + 1):
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    student_sum_dict = {}
    student_result_dict = {}
    Output = [1] * N
    student_list = []
    student_list_reverse = []
    for i in range(N):
        student = list(map(int, input().split()))

        # 학생의 성적을 입력 받아 점수를 계산한 리스트
        student_list.append((student[0] * 0.35) + (student[1] * 0.45) + (student[2] * 0.2))

        # 학생의 성적을 입력 받아 점수를 계산한 리스트(다음 코드에서 내림차순으로 정렬)
        student_list_reverse.append((student[0] * 0.35) + (student[1] * 0.45) + (student[2] * 0.2))

    student_list_reverse.sort(reverse=True)

    # 오름차순한 점수를 key로 하고 높은 점수대로 함수에서 구한 학점을 부여
    for i in range(N):
        student_result_dict[student_list_reverse[i]] = student_score(score)[i]

    # 처음 입력 받은 학생 순서대로 학점을 다시 넣어준 리스트
    for i in range(N):
        Output[i] = student_result_dict[student_list[i]]

    print(f"#{test_case} {Output[K - 1]}")