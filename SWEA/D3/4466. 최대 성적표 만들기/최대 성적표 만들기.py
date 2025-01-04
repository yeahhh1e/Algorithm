T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))

    # 점수 리스트 내림차순 정렬
    sorted_score = sorted(score_list, reverse=True)

    max_sum = 0
    # K개만큼 더해주기
    for i in range(K):
        max_sum += sorted_score[i]

    print(f'#{tc} {max_sum}')