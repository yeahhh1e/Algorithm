import sys
import pprint
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))
    # print(matrix)

    # 가운데 좌표 위치
    C = N // 2
    total = 0
    for i in range(0, C+1):   # 처음~ 가운데까지 더하기
        total += matrix[C][i] # 가운데 줄 더하기
        for j in range(1, i+1):   # 해당 열 더해주기
            if C-j >= 0 and C+j < N:
                total += matrix[C-j][i]
                total += matrix[C+j][i]

    for x in range(N-1, C, -1): # 끝에서부터 가운데 다음줄까지 더하기
        total += matrix[C][x]  # 가운데 줄 더하기
        if x < (N-1): # 마지막 열 제외하고 순회
            for y in range(1, C):   # 해당 열 더해주기
                if C-y >= 0 and C+y < N:
                    total += matrix[C-y][x]
                    total += matrix[C+y][x]

    print(f'#{tc} {total}')