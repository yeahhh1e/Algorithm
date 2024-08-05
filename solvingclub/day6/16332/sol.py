import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    MN_list = list(map(int,input().split()))
    M = MN_list[0]
    N = MN_list[1]
    str_list = []
    for i in range(M):
        
        str_list.append(list(map(str, input().split())))
    print(M, N ,str_list)