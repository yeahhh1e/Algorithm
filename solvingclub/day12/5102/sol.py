import sys
sys.stdin = open("input.txt", "r")

def bfs(s, V, g):  # 시작정점 s, 마지막 정점 V, 도착정점 g
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        # print(t)  # 방문한 정점에서 할일
        for w in matrix[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1
    return visited[g] - 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_info = []
    for n in range(E):
        
        edge_info.append(list(map(int, input().split())))
    # print(edge_info)
    S, G = map(int, input().split())
    matrix = []
    # for i in range(V+1):
    #     matrix.append([]) 
    # print(matrix)
    # # print(V, E, edge_info, S, G)
    # for i in edge_info:
    #     matrix[i[0] + 1][i[1]+ 1] = matrix[i[1] + 1][i[0] + 1] = 1
    # print(matrix)

    # print(bfs(S, V, G))

    # cnt = [0]*(V+1)
    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         if matrix[i][j] == 1:
    #             cnt[j] += 1

    for _ in range(V + 1):
        matrix.append([])
    for li in edge_info:
        matrix[li[0]].append(li[1])
        matrix[li[1]].append(li[0])
    # print(matrix)

    print(bfs(S, V, G))
