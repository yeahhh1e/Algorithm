import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    # print(M_list)
    # M_list M쌍으로 만들기
    application_list = []
    for i in range(0, len(M_list), 2):
        application_list.append(M_list[i:i+2])

    group_list = []
    for i in range(M):  # 신청 리스트를 순회하며 집합 생성
        check = False
        for j in range(2):
            for x in group_list:
                if application_list[i][j] in x: # group_list에 application 요소가 있으면 해당 리스트에 전체 추가
                    x.extend(application_list[i])
                    check = True
                    break
            if check: # 리스트에 이미 추가했으면 멈추기
                break
        else: # group_list에 없으면
            group_list.append(application_list[i]) # 새로운 리스트로 추가

    result = len(group_list)
    new_group_list = list(set([tuple(set(item)) for item in group_list]))
    print(new_group_list)

    # 교집합이 있는 경우 result -= 1
    for i in range(len(group_list)):
        for j in range(i+1, len(group_list)):
            inter_set = set(group_list[i]) & set(group_list[j])
            if len(inter_set) >= 1:
                result -= 1
            if set(group_list[i]) == set(group_list[j]): # 만약 i와 j가 같은 경우 추가로 더 빼주기
                result -= 1
    # group_list 순회하면서 신청 안 된 사람 확인
    for i in range(1, N+1): # i가 group_list에 없으면 result += 1
        check = False
        for j in range(0, len(group_list)):
            if i in group_list[j]:
                check = True
                break
        if check == False:
            result += 1

    print(f"#{tc} {result}")
