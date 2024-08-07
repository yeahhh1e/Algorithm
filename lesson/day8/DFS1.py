'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(s, V):              # s: 시작정점, V: 정점개수(1번부터인 정점의마지막 정점)
    visited = [0]*(V+1)     # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작정점 방문표시
    v = s                   # v: 현재 정점
    
    while True:
        for w in adjL[v]:    # v에 인접하고, 방문 안 한 w가 있으면 (adjL[v]에 인접한 정점만 저장했기 때문에)
            if visited[w] == 0:     # w도 인접한 정점만 나올 것 / 남아있는 정점이 없을 경우
                stack.append(v) # push(v) 현재 정점을 push하고
                v = w           # 현재 정점 = w
                print(v)
                visited[w] = 1  # w에 방문 표시
                break           # for w에 대한 break, v부터 다시 탐색
        else:      # for else 구문 # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack:    # 이전 갈림길을 스택에서 꺼내서 ... if TOP > -1 (TOP 사용 시 스택이 남은게 있는 경우)
                v = stack.pop()
            else:               # 되돌아갈 곳이 없으면 남은 갈림길이 없으므로 탐색 종료
                break           # while True에 대한 break

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V = 마지막 정점
    # E = 간선 수
    
    # adj[1] -> 1에 인접인 정점
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):  # 2개씩 읽기
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)
