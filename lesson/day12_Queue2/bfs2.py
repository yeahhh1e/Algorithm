def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)]# visited 생성
    q = []  # 큐생성
    q.append([i, j])    # 시작점 인큐
    visited[i][j] = 1   # 시작점 인큐 표시

    # 탐색
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3: # visited(t)
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수,
        for di, dj in [[0, 1], [1, 0], []]

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

N = int(input())
maze = [list(map(int, input())) for]
