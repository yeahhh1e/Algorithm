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

    # 두번째줄부터 아래서 세번째 줄까지 흰색으로 바꾸는 함수
    def change_w(lst):
        global cnt
        for i in range(1, N-2):
            for j in range(M):
                if lst[i][j] != 'W':
                    cnt += 1
    
    # 각 줄마다 가장 많은 색 찾는 함수
    def find_most_color(lst):
        global W
        global B
        global R
        global most_color_j
        global most_color
        most_color = {'B': 0, 'W': 0, 'R': 0}
        for i in range(1, N-1):
            W = B = R = 0
            most_color_j = {'B': 0, 'W': 0, 'R': 0}
            for j in range(M):
                if lst[i][j] == 'B':
                    most_color_j['B'] += 1
                elif lst[i][j] == 'W':
                    most_color_j['W'] += 1
                else:
                    most_color_j['R'] += 1
            if most_color_j['B'] == most_color_j['W']:
                c = 'B'
            else:
                c = max(most_color_j)
            print(c)
            most_color[c] += 1
        if most_color['B'] == most_color['W']:
            result = 'B'
        else:
            result = max(most_color)
        return result
    # 아래서 두번째줄 빨강으로 바꾸는게 나은 경우..
    most_color = find_most_color(color_list)
    if most_color == 'W':   # 두번째줄 부터 아래서 세번째줄까지 흰색으로 바꾸기
        # 만약 네번째줄까지만 있는 경우 여유가 없으므로 두번째줄까지만 흰색으로 바꾸기
        if N <= 4:
            for j in range(M):
                if color_list[1][j] != 'W':
                    cnt += 1
        elif N > 4:
            for i in range(1, N-2):
                for j in range(M):
                    if color_list[i][j] != 'W':
                        cnt += 1

        # 아래서 두번째 줄 파란색으로 바꾸기
        for n in range(M):
            if color_list[-2][n] != 'B':
                cnt += 1
            
    elif most_color == 'B': # 두번째줄부터 아래서 두번째줄까지 파란색으로 바꾸기
        for i in range(1, N-1):
            for j in range(M):
                if color_list[i][j] != 'B':
                    cnt += 1
    else:                   # 세번째줄부터 아래서 두번째줄까지 빨간색으로 바꾸기
        for i in range(1, N-1):
            for j in range(M):
                if color_list[i][j] != 'B':
                    cnt += 1
        # 위에서 두번째 줄 파란색으로 바꾸기
        for n in range(M):
            if color_list[-2][n] != 'B':
                cnt += 1
    
    print(cnt)





    
        


    


    # # 두번째 줄은 흰색 or 파랑이어야 함 ( 둘 중 최솟값인 것으로 )
    # W = 0
    # B = 0
    # for i in range(M):
    #     if color_list[1][i] == 'W':
    #         W += 1
    #     elif color_list[1][i] == 'B':
    #         B += 1
    # if W >= B: # W가 더 많으면 W로 바꾸기
    #     cnt += M-W # 흰색 제외하고 바꿈
    #     # 나머지 줄은 흰 or 파 or 빨
    #     for i in range(2, N - 1):
    #         B = 0
    #         R = 0
    #         for j in range(M):
    #             if color_list[i][j] == 'B':
    #                 B += 1
    #             elif color_list[i][j] == 'R':
    #                 R += 1
    #         if B >= R:  # B가 더 많으면 B로 바꾸기
    #             cnt += M - B  # 파랑색 제외하고 바꿈
    #         else:
    #             cnt += M - R
    # else:
    #     cnt += M-B

    # # 나머지줄은 파 or 빨
    # for i in range(2, N-1):
    #     B = 0
    #     R = 0
    #     for j in range(M):
    #         if color_list[i][j] == 'B':
    #             B += 1
    #         elif color_list[i][j] == 'R':
    #             R += 1
    #     if B >= R:  # B가 더 많으면 B로 바꾸기
    #         cnt += M - B  # 파랑색 제외하고 바꿈
    #     else:
    #         cnt += M - R

    # print(cnt)
