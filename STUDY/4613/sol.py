import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(N, M)
    color_list = []
    for _ in range(N):
        color_list.append(list(map(str, input())))

    # print(color_list)

    cnt = 0
    # 첫번째줄은 흰색으로 바꿔주기
    for i in range(M):
        if color_list[0][i] != 'W':
            cnt += 1
    # 마지막 줄은 빨간색으로 바꿔주기
    for i in range(M):
        if color_list[-1][i] != 'R':
            # color_list[-1][i] = 'R'
            cnt += 1

    # 두번째 줄은 흰색 or 파랑이어야 함 ( 둘 중 최솟값인 것으로 )
    W = 0
    B = 0
    for i in range(M):
        if color_list[1][i] == 'W':
            W += 1
        elif color_list[1][i] == 'B':
            B += 1
    if W >= B: # W가 더 많으면 W로 바꾸기
        cnt += M-W # 흰색 제외하고 바꿈
        # 나머지 줄은 흰 or 파 or 빨
        for i in range(2, N - 1):
            B = 0
            R = 0
            for j in range(M):
                if color_list[i][j] == 'B':
                    B += 1
                elif color_list[i][j] == 'R':
                    R += 1
            if B >= R:  # B가 더 많으면 B로 바꾸기
                cnt += M - B  # 파랑색 제외하고 바꿈
            else:
                cnt += M - R
    else:
        cnt += M-B

    # 나머지줄은 파 or 빨
    for i in range(2, N-1):
        B = 0
        R = 0
        for j in range(M):
            if color_list[i][j] == 'B':
                B += 1
            elif color_list[i][j] == 'R':
                R += 1
        if B >= R:  # B가 더 많으면 B로 바꾸기
            cnt += M - B  # 파랑색 제외하고 바꿈
        else:
            cnt += M - R

    print(cnt)
