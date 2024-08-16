import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 터트린 풍선에서 나오는 꽃가루 개수
            for k in range(4):
                for l in (1, arr [i][j]+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]  # 주변의 풍선에서 나오는 꽃가루 추가
        if max_v < cnt:   # for k에서 모든 꽃가루가 더해졌기 때문에
                max_v = cnt
                        
    print(f'#{tc} {max_v}')