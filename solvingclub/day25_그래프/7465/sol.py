import sys
sys.stdin = open("s_input.txt", "r")

def dfs(node):
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [[0] * (N + 1)] * (N + 1)

    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)


    visited[1] = 1
    dfs(1)
