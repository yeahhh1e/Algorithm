import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    max_sum = 0 # 최대값 저장할 변수 설정
    for i in range(N):
        for j in range(M):
            total = 0
            total += matrix[i][j]   # 아래 for문에 넣을경우 제자리도 n번만큼 더해지므로 위에서 따로 더해주기
            for n in range(1, matrix[i][j]+1):
                for x, y in ((i, j+n), (i+n, j), (i, j-n), (i-n, j)):   # 해당 값만큼 주변 더 더해주기
                    if 0 <= x < N and 0 <= y < M:
                        total += matrix[x][y]
            if max_sum < total:
                max_sum = total
                        
    print(f'#{tc} {max_sum}')