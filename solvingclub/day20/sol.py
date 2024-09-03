import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w_list = list(map(int, input().split()))    # N개
    t_list = list(map(int, input().split()))    # M개

    # 내림차순으로 정렬해주기
    w_list.sort(reverse=True)
    t_list.sort(reverse=True)

    total = 0
    # while t_list:
    for i in range(N):
        if len(t_list) == 0:
            break
        M = len(t_list) # 컨테이너 수 갱신
        for j in range(M):
            if w_list[i] <= t_list[j]: # 화물의 무게가 제일 큰 적재용량 이하라면
                total += w_list[i] # 무게 추가하고
                t_list.pop(j) # 해당 컨테이너 빼주기
                break
            else: # 해당 화물을 넣을 수 있는 컨테이너가 없으면
                continue

    print(f"#{tc} {total}")