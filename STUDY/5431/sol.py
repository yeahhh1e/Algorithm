import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit_list = list(map(int, input().split()))

    # print(N, K, submit_list)

    check_list = [0] * (N+1) # 체크리스트 만들기 (0번 인덱스는 없는 사람)
    # 제출자 리스트를 순회하며 해당 번호의 사람은 1로 바꿔주기
    for s in submit_list:
        check_list[s] = 1

    Non_submit = []
    # 체크리스트를 순회하며 0인 사람들은 미제출자이므로 해당 인덱스만 모으기
    for i in range(1, N+1):
        if check_list[i] == 0:
            Non_submit.append(i)
    
    # 0번은 없는 사람이므로 빼주기
    print(f'#{tc} ', end= "")   # tc 뒤에 공백 넣어야 Non_submit의 첫번째 1이 안 붙음
    print(*Non_submit)