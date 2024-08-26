import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append((list(input())))

    result = 'NO'
    check = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o': # 해당 자리에 돌이 있으면
                cnt = 0
                for x, y in ((i, j+1), (i+1, j), (i, j-1), (i-1, j), (i+1, j+1), (i+1, j-1)):   # 상하좌우대각선 탐색
                    check = 0   # 처음 체크값 0
                    cnt += 1    # 어느 방향으로 돌이 있는지 체크하기 위한 cnt 변수 설정
                    if 0 <= x < N and 0 <= y < N and matrix[x][y] == 'o':   # 인덱스 범위 안이고 해당자리에 돌이 있으면
                        if cnt == 1:    # 오른쪽으로 다섯개인지 체크
                            for m in range(5):
                                if 0 <= x < N and 0 <= y+m < N and matrix[x][y+m] == 'o':
                                    check += 1
                        elif cnt == 2: # 아래쪽으로 다섯 개인지 체크
                            for m in range(4):
                                if 0 <= x+m < N and 0 <= y < N and matrix[x+m][y] == 'o':
                                    check += 1
                        elif cnt == 3:    # 왼쪽으로 다섯 개인지 체크
                            for m in range(4):
                                if 0 <= x < N and 0 <= y-1 < N and matrix[x][y-1] == 'o':
                                    check += 1
                        elif cnt == 4:    # 위로 다섯 개인지 체크
                            for m in range(4):
                                if 0 <= x-1 < N and 0 <= y < N and matrix[x-1][y] == 'o':
                                    check += 1
                        elif cnt == 5: # 오른쪽 아래 대각선으로 다섯 개인지 체크
                            for m in range(4):
                                if 0 <= x+m < N and 0 <= y+m < N and matrix[x+m][y+m] == 'o':
                                    check += 1
                        elif cnt == 6:  # 왼쪽 아래 대각선으로 다섯 개인지 체크
                            for m in range(4):
                                if 0 <= x+m < N and 0 <= y-m < N and matrix[x+m][y-m] == 'o':
                                    check += 1
                    if check == 4:  # 돌이 5개가 있으면 for문 종료
                        result = 'YES'
                        break

    print(f'#{tc} {result}')