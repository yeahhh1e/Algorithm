import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    MN_list = list(map(int,input().split()))
    M = MN_list[0] # 행
    N = MN_list[1] # 열
    str_list = []
    for i in range(M):
        str_list.append(list(map(str, input().split())))
    print(M, N ,str_list)

    # 가로 탐색 (행 탐색)
    n = N # 구간의 길이
    m = M # 패턴의 길이
    i = 0 
    j = 0

    while i < n and j < m:
        if str_list[0]